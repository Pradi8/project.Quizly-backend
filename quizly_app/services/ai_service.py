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
    Erstelle genau 10 Quizfragen aus dem Text.

    Format:

    {{
    "title": "string",
    "description": "string",
    "questions": [
        {{
            "question_title": "string",
            "question_options": ["A", "B", "C", "D"],
            "answer": "string"
        }}
    ]
}}

Text:
{text}

    """

    response = model.generate_content(prompt)
    if not response.text:
        raise ValueError("Leere Antwort von Gemini")
    return response.text

def parse_quiz_json(raw):

    if not raw:
        raise ValueError("Empty Gemini response")

    cleaned = raw.strip()

    # 🔥 Entfernt Markdown fences sicher
    cleaned = re.sub(r"^```(?:json)?", "", cleaned)
    cleaned = re.sub(r"```$", "", cleaned).strip()

    # 🔥 extrahiere erstes JSON Objekt (wichtig!)
    match = re.search(r"\{.*\}|\[.*\]", cleaned, re.DOTALL)
    if match:
        cleaned = match.group(0)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        raise