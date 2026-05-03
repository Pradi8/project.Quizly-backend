from .services.ai_service import generate_quiz, parse_quiz_json
from .models import Question, Quiz

def process_video(quiz_id, video_url):
   
    quiz = Quiz.objects.get(id=quiz_id)

    # 🔥 Whisper + Gemini
    result = generate_quiz(video_url)
    data = parse_quiz_json(result)

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