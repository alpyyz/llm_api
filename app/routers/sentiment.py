from fastapi import APIRouter
from app.services.sentiment_service import analyze_sentiment
from app.models.schemas import TextRequest

router = APIRouter()

@router.post("/")
def sentiment_analysis(request: TextRequest):
    """
    Accepts text and returns its sentiment label.
    """
    return {"sentiment": analyze_sentiment(request.text)}
