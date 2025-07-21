from fastapi import APIRouter
from app.models.schemas import SummarizationRequest, SummarizationResponse
from app.services.summarization_service import summarize

router = APIRouter(prefix="/summarization", tags=["summarization"])

@router.post("/", response_model=SummarizationResponse)
def summarization_endpoint(req: SummarizationRequest):
    summary = summarize(req.text)
    return SummarizationResponse(summary=summary)
