from typing import Union
from fastapi import FastAPI
from models.HealthResponse import HealthResponse
from models.ClassificationRequest import ClassificationRequest
from services.ImageClassificationService import ImageClassificationService

# Classification
classification_service = ImageClassificationService()

# Fast API
app = FastAPI()


# ===== ENDPOINTS =====
@app.get('/health')
async def get_health():
    return HealthResponse


@app.post('/detection/classify_image')
async def post_classify_image(request: ClassificationRequest):
    image = request.b64_encoded_image
    return classification_service.classify_image(image)


@app.post('/detection/bounding_boxes')
async def post_get_bounding_boxes(request: ClassificationRequest):
    return {'NOT IMPLEMENTED YET!'}
