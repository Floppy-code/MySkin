from pydantic import BaseModel


class ClassificationRequest(BaseModel):
    b64_encoded_image: str
