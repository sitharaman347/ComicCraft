
from pydantic import BaseModel, Field


class ComicRequest(BaseModel):
    prompt: str = Field(..., min_length=1)


class ComicOutline(BaseModel):
    title: str
    characters: list[str]
    setting: str
    beginning: str
    middle: str
    ending: str
    panels: list[str]


class StoryRequest(BaseModel):
    outline: str = Field(..., min_length=1)


class ImageRequest(BaseModel):
    prompt: str = Field(..., min_length=1)