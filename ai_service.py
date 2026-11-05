import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("AI_API_KEY"))
MODEL_NAME = os.getenv("AI_MODEL", "gemini-3.8-flash")


def summarize_text(text: str) -> str:
    prompt = f"Summarize the following note in 2-3 short sentences:\n\n{text}"
    response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
    return response.text