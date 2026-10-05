
import requests

from app.config import (
    HF_TOKEN,
    HF_IMAGE_MODEL,
    IMAGE_WIDTH,
    IMAGE_HEIGHT,
    IMAGE_STEPS,
)


def generate_image(prompt: str) -> bytes:
    """Generate a comic image using Hugging Face."""

    if not HF_TOKEN:
        raise ValueError("HF_TOKEN is missing in .env")

    if not prompt or not prompt.strip():
        raise ValueError("Image prompt cannot be empty")

    url = f"https://router.huggingface.co/hf-inference/models/{HF_IMAGE_MODEL}"

    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "width": IMAGE_WIDTH,
            "height": IMAGE_HEIGHT,
            "num_inference_steps": IMAGE_STEPS,
        },
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=180,
    )

    response.raise_for_status()

    return response.content