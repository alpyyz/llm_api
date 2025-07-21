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

class SummarizationRequest(BaseModel):
    text: str

class SummarizationResponse(BaseModel):
    summary: str

class EmbeddingRequest(BaseModel):
    text: str

class EmbeddingResponse(BaseModel):
    embedding: List[float]