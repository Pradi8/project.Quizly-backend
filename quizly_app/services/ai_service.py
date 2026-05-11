import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_quiz(text):
    prompt = f"""
      
    Based on the following transcript, generate a quiz in valid JSON format.

    The quiz must follow this exact structure:

    {{

        "title": "Create a concise quiz title based on the topic of the transcript.",

        "description": "Summarize the transcript in no more than 150 characters. Do not include any quiz questions or answers.",

        "questions": [

        {{

            "question_title": "The question goes here.",

            "question_options": ["Option A", "Option B", "Option C", "Option D"],

            "answer": "The correct answer from the above options"

        }},

        ...

        (exactly 10 questions)

        ]

    }}

    Requirements:

    - Each question must have exactly 4 distinct answer options.

    - Only one correct answer is allowed per question, and it must be present in 'question_options'.

    - The output must be valid JSON and parsable as-is (e.g., using Python's json.loads).

    - Do not include explanations, comments, or any text outside the JSON.

    transcript:
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