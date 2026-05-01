from .services.youtube_service import download_audio
from .services.audio_service import transcribe_audio
from .services.ai_service import generate_quiz, parse_quiz_json
from .models import Question, Quiz
from django.db import transaction
from rq import Queue
from redis import Redis

def process_video(quiz_id, url):
    quiz = Quiz.objects.get(id=quiz_id)

    quiz.status = "downloading"
    quiz.save(update_fields=["status"])

    file_path, info = download_audio(url, quiz_id)

    quiz.status = "transcribing"
    quiz.save(update_fields=["status"])

    text = transcribe_audio(file_path)

    quiz.title = info.get("title", "")
    quiz.description = info.get("description", "")
    quiz.transcript = text
    quiz.status = "transcribed"
    quiz.save()

    # RQ NEXT JOB
    r = Redis()
    q = Queue(connection=r)

    q.enqueue(generate_quiz_task, quiz.id, text)


def generate_quiz_task(quiz_id, text):
    quiz = Quiz.objects.get(id=quiz_id)

    quiz.status = "generating"
    quiz.save(update_fields=["status"])
    
    raw = generate_quiz(text)
    data = parse_quiz_json(raw)

    with transaction.atomic():
        Question.objects.filter(quiz=quiz).delete()

        Question.objects.bulk_create([
            Question(
                quiz=quiz,
                question_title=item["question"],
                question_options=item["options"],
                answer=item["answer"],
            )
            for item in data
            if all(k in item for k in ("question", "options", "answer"))
        ])

    quiz.status = "done"
    quiz.save(update_fields=["status"])