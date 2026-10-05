
from google import genai

from app.config import GEMINI_API_KEY, GEMINI_STORY_MODEL


if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_story(outline: str) -> str:
    """
    Generate a detailed comic story from the outline.
    """

    if not outline or not outline.strip():
        raise ValueError("Outline cannot be empty")

    response = client.models.generate_content(
        model=GEMINI_STORY_MODEL,
        contents=(
            "Turn the following comic outline into a detailed comic script.\n\n"
            f"Outline:\n{outline}\n\n"
            "For each panel include:\n"
            "- Scene description\n"
            "- Character actions\n"
            "- Dialogue\n"
            "- Background\n"
            "- Camera angle\n"
        ),
    )

    return response.text or ""