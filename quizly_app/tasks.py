import os

from quizly_app.services.audio_service import transcribe_audio
from quizly_app.services.youtube_service import download_audio
from .services.ai_service import generate_quiz, parse_quiz_json
from .models import Question, Quiz

def process_video(quiz_id, video_url):
    """
    Main function to process the video for a given quiz
    """

    # Step 1: Download the audio from the YouTube URL
    file_path = download_audio(video_url)

    # Step 2: Transcribe the audio to text
    audio_text = transcribe_audio(file_path)

    # Step 3: Generate quiz content in JSON format
    result = generate_quiz(audio_text)
    # Step 4: Parse the generated quiz JSON and save it to the database
    data = parse_quiz_json(result)

    # Step 5: Update the Quiz instance with the generated title, description, and questions
    quiz = Quiz.objects.get(id=quiz_id)

    quiz.title = data.get("title", "")
    quiz.description = data.get("description", "")
    quiz.save()

    # Create Question instances for each question in the generated quiz
    for q in data.get("questions", []):
        Question.objects.create(
            quiz=quiz,
            question_title=q["question_title"],
            question_options=q["question_options"],
            answer=q["answer"]
        )
    
    # Step 6: Clean up the downloaded audio file
    if os.path.exists(file_path):
        os.remove(file_path)