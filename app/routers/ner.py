from fastapi import APIRouter
from app.services.ner_service import extract_entities
from app.models.schemas import TextRequest

router = APIRouter()

@router.post("/")
def named_entity_recognition(request: TextRequest):
    """
    Accepts text and returns extracted named entities.
    """
    return {"entities": extract_entities(request.text)}
