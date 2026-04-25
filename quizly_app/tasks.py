from .services.youtube_service import download_audio
from .services.audio_service import transcribe_audio
from .services.ai_service import generate_quiz
from .models import Question, Quiz
import json
import logging
from django.db import transaction

logger = logging.getLogger(__name__)

def process_video(quiz_id, url):
    """
    Generate a quiz from a video URL and store it in the database.
    """
    try:
        quiz = Quiz.objects.get(id=quiz_id)

        # Mark as processing early so UI/jobs know this task is running
        quiz.status = "processing"
        quiz.save(update_fields=["status"])

        # Download audio from the video and get metadata (title, description)
        file_path, info = download_audio(url, quiz_id)

        # Convert audio file to text (transcription)
        text = transcribe_audio(file_path)

        # External AI may return invalid JSON → can raise
        data = json.loads(generate_quiz(text))

       # Ensure we don't end up with partially written data
        with transaction.atomic():
            # Update quiz fields with new data
            quiz.title = info.get("title", "")
            quiz.description = info.get("description", "")
            quiz.transcript = text
            quiz.save()

            # Remove existing questions to avoid duplicates
            Question.objects.filter(quiz=quiz).delete()

            # Create new questions in bulk
            Question.objects.bulk_create([
                Question(
                    quiz=quiz,
                    question_title=item["question"],
                    question_options=item["options"],
                    answer=item["answer"],
                )
                # Only include valid question items
                for item in data
                if all(k in item for k in ("question", "options", "answer"))
            ])

        quiz.status = "done"
        quiz.save(update_fields=["status"])

    except Exception as e:
        # Critical: log full stacktrace for debugging in production
        logger.exception(f"Quiz {quiz_id} failed: {e}")
        # Use update() to avoid issues if object is stale
        Quiz.objects.filter(id=quiz_id).update(status="failed")