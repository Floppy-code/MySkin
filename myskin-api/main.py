import uvicorn
from typing import Union
from fastapi import FastAPI
from typing import List
from models.ClassificationRequest import ClassificationRequest
from models.ClassificationResponse import ClassificationResponse
from services.ImageClassificationService import ImageClassificationService
from fastapi.middleware.cors import CORSMiddleware

# Classification
classification_service = ImageClassificationService()

# Fast API
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===== ENDPOINTS =====
@app.get('/health')
async def get_health():
    return {"Status": "Healthy"}


@app.post('/detection/classify_image')
async def post_classify_image(request: ClassificationRequest):
    image = request.b64_encoded_image.split(",")[1]
    return classification_service.classify_image(image)


@app.post('/detection/bounding_boxes')
async def post_get_bounding_boxes(request: ClassificationRequest):
    return {'NOT IMPLEMENTED YET!'}

def run():
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info", workers=4, loop="uvloop")

if __name__ == "__main__":
    run()