import os

from quizly_app.services.audio_service import transcribe_audio
from quizly_app.services.youtube_service import download_audio
from .services.ai_service import generate_quiz, parse_quiz_json
from .models import Question, Quiz

def process_video(quiz_id, video_url):
    print("1. Download startet")
    file_path = download_audio(video_url)

    print("2. Whisper startet")
    audio_text = transcribe_audio(file_path)
    
    print("3. Gemini startet")
    result = generate_quiz(audio_text)
    data = parse_quiz_json(result)

    print("4. Fertig")
    quiz = Quiz.objects.get(id=quiz_id)

    quiz.title = data.get("title", "")
    quiz.description = data.get("description", "")
    quiz.save()

    for q in data.get("questions", []):
        Question.objects.create(
            quiz=quiz,
            question_title=q["question_title"],
            question_options=q["question_options"],
            answer=q["answer"]
        )
    if os.path.exists(file_path):
        os.remove(file_path)