from fastapi import APIRouter
from app.models.introduction_extraction_service import IntroductionRequest, IntroductionResponse
from app.services.introduction_extraction_service import extract_introduction, get_embedding

router = APIRouter(prefix="/introduction", tags=["introduction"])

@router.post("/", response_model=IntroductionResponse)
def introduction_endpoint(req: IntroductionRequest):
    intro_text = extract_introduction(req.raw_text)
    embedding = get_embedding(intro_text)
    return IntroductionResponse(
        introduction_text=intro_text,
        embedding=embedding
    )
