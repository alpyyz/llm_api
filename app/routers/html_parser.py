from fastapi import APIRouter
from app.services.html_service import parse_html
from app.models.schemas import TextRequest

router = APIRouter()

@router.post("/")
def html_understanding(request: TextRequest):
    """
    Accepts HTML and returns the extracted main text.
    """
    return {"parsed": parse_html(request.text)}
