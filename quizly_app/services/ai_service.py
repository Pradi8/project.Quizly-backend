import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def generate_quiz(text):
    prompt = f"""
    Erstelle 10 Quizfragen aus diesem Text:

    {text}
    [
        {{
            "question": "...",
            "options": ["A", "B", "C", "D],
            "answer": "..."
        }}
    ]
    """

    response = model.generate_content(prompt)
    return response.text