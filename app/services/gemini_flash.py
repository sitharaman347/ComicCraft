
from google import genai

from app.config import GEMINI_API_KEY, GEMINI_OUTLINE_MODEL


if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY is missing in .env")


client = genai.Client(api_key=GEMINI_API_KEY)


def generate_outline(prompt: str) -> str:
    """
    Generate a comic/story outline using Gemini Flash.
    """

    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")

    response = client.models.generate_content(
        model=GEMINI_OUTLINE_MODEL,
        contents=(
            "Create a clear comic story outline from the following idea.\n\n"
            f"Story idea:\n{prompt}\n\n"
            "Include:\n"
            "1. Title\n"
            "2. Main characters\n"
            "3. Setting\n"
            "4. Beginning\n"
            "5. Middle\n"
            "6. Ending\n"
            "7. Panel-by-panel outline"
        ),
    )

    return response.text or ""