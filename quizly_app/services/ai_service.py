import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model = genai.GenerativeModel("gemini-1.5-flash")
model = genai.GenerativeModel("gemini-2.5-flash")

def generate_quiz(text):
    prompt = f"""
    Du bist ein strikter JSON-Generator.

    Erstelle aus dem folgenden Text genau 10 Quizfragen.

    WICHTIGE REGELN:
        - Antworte NUR mit gültigem JSON
        - Kein zusätzlicher Text
        - Kein Markdown
        - Keine Erklärungen

    {text}
    [
        {{
            "question": "...",
            "options": ["A", "B", "C", "D"],
            "answer": "..."
        }}
    ]
    """

    response = model.generate_content(prompt)
    if not response.text:
        raise ValueError("Leere Antwort von Gemini")
    return response.text

def parse_quiz_json(raw_text):
    cleaned = raw_text.strip()

    # entfernt ```json ... ```
    cleaned = re.sub(r"^```json", "", cleaned)
    cleaned = re.sub(r"```$", "", cleaned)
    cleaned = cleaned.strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        raise