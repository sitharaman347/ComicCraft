import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_OUTLINE_MODEL = os.getenv(
    "GEMINI_OUTLINE_MODEL",
    "gemini-2.5-flash"
)

GEMINI_STORY_MODEL = os.getenv(
    "GEMINI_STORY_MODEL",
    "gemini-2.5-pro"
)

HF_TOKEN = os.getenv("HF_TOKEN")

HF_IMAGE_MODEL = os.getenv(
    "HF_IMAGE_MODEL",
    "black-forest-labs/FLUX.1-schnell"
)

IMAGE_WIDTH = int(os.getenv("IMAGE_WIDTH", "768"))
IMAGE_HEIGHT = int(os.getenv("IMAGE_HEIGHT", "768"))
IMAGE_STEPS = int(os.getenv("IMAGE_STEPS", "4"))