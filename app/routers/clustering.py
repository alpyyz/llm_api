from fastapi import APIRouter
from app.services.clustering_service import cluster_documents
from app.models.schemas import TextListRequest

router = APIRouter()

@router.post("/")
def cluster_texts(request: TextListRequest):
    """
    Accepts a list of texts and returns their cluster assignments.
    """
    return {"clusters": cluster_documents(request.texts)}
