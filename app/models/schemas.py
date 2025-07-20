from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text: str

class TextListRequest(BaseModel):
    texts: List[str]
