from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text: str

class TextListRequest(BaseModel):
    texts: List[str]

class IntroductionExtractionRequest(BaseModel):
    raw_text: str

class IntroductionExtractionResponse(BaseModel):
    introduction_text: str
    embedding: List[float]
