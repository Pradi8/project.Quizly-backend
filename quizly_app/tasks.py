from .services.youtube_service import download_audio
from .services.audio_service import transcribe_audio
from .services.ai_service import generate_quiz
from .models import Question, Quiz
import json


def process_video(quiz_id, url):

    file_path, info = download_audio(url, quiz_id)

    text = transcribe_audio(file_path)

    quiz_json = generate_quiz(text)

    quiz = Quiz.objects.get(id=quiz_id)
    quiz.title = info.get("title")
    quiz.description = info.get("description")
    quiz.transcript = text
    quiz.status = "processing"
    quiz.save()

    # 👉 JSON parsen
    data = json.loads(quiz_json)

    # 👉 Fragen speichern
    for item in data:
        Question.objects.create(
            quiz=quiz,
            question_title=item["question"],
            question_options=item["options"],
            answer=item["answer"]
        )

    quiz.status = "done"
    quiz.save()