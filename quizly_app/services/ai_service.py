import google.generativeai as genai
import os
from dotenv import load_dotenv
import json
import re

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_quiz(text):
    """
    Return ONLY valid JSON.
    No explanations.
    No markdown.
    All keys must use double quotes.
    Generates a quiz in JSON format based on the provided transcript text using Gemini API.
    """

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
        raise ValueError("Empty Gemini response")
    return response.text

def parse_quiz_json(raw):
    """
    Parses and cleans the raw Gemini API response
    and converts it into a Python dictionary or list.

    Removes markdown code block formatting (```json ... ```)
    and extracts valid JSON content before parsing.
    """

    # Check if the response is empty or None
    if not raw:
        raise ValueError("Empty Gemini response")

    # Remove leading and trailing whitespace
    cleaned = raw.strip()

    # Remove opening markdown code block markers
    # Example: ```json
    cleaned = re.sub(r"^```(?:json)?", "", cleaned)

    # Remove closing markdown code block markers
    # Example: ```
    cleaned = re.sub(r"```$", "", cleaned).strip()

    # Search for the first valid JSON object ({...})
    # or JSON array ([...]) inside the cleaned text
    match = re.search(r"\{.*\}|\[.*\]", cleaned, re.DOTALL)

    # If JSON content is found, extract only that part
    if match:
        cleaned = match.group(0)

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        raise