from pydantic import BaseModel


class ClassificationResponse(BaseModel):
    id: int
    name: str
    probability: float
