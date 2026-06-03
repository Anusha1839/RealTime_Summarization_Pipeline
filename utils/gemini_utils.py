import os
from dotenv import load_dotenv
import google.generativeai as genai
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-flash-latest")


def generate_structured_summary(text):

    prompt = f"""
Analyze the transcript.

Return ONLY valid JSON.

Format:

{{
    "title": "",
    "summary": {{
        "overview": "",
        "problem": "",
        "solution": ""
    }},
    "key_points": [
        {{
            "point": ""
        }}
    ],
    "action_items": [
        {{
            "action": ""
        }}
    ]
}}

Transcript:
{text}
"""

    response = model.generate_content(prompt)

    return json.loads(response.text)