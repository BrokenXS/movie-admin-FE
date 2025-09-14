from pydantic import BaseModel
from typing import Optional

class MovieModel(BaseModel):
    id: Optional[int]
    title: str
    description: Optional[str] = None
    year: Optional[int] = None
