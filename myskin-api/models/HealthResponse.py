from pydantic import BaseModel


class HealthResponse(BaseModel):
    message: str = 'Status'
    status: str = 'Healthy'
