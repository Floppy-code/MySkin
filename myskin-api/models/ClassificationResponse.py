from typing import List
from pydantic import BaseModel


class ClassificationResponse(BaseModel):
    label_id: int
    label_name: str
    probability: float
