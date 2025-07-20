from fastapi import APIRouter
from app.models.schemas import IntroductionExtractionRequest, IntroductionExtractionResponse
from app.services.introduction_extraction_service import extract_introduction, get_embedding

router = APIRouter(prefix="/introduction", tags=["introduction"])

@router.post("/", response_model=IntroductionExtractionResponse)
def introduction_endpoint(req: IntroductionExtractionRequest):
    intro_text = extract_introduction(req.raw_text)
    embedding = get_embedding(intro_text)
    return IntroductionExtractionResponse(
        introduction_text=intro_text,
        embedding=embedding
    )
