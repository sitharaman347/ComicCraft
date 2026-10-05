
from fastapi import APIRouter, HTTPException

from app.schemas import ComicRequest, StoryRequest
from app.services.gemini_flash import generate_outline
from app.services.gemini_pro import generate_story

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/outline")
def create_outline(request: ComicRequest):
    try:
        outline = generate_outline(request.prompt)
        return {
            "success": True,
            "outline": outline,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/story")
def create_story(request: StoryRequest):
    try:
        story = generate_story(request.outline)
        return {
            "success": True,
            "story": story,
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))