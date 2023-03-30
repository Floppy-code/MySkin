import io
from models.ClassificationResponse import ClassificationResponse
import base64
import numpy as np
from PIL import Image
from skimage.transform import resize
from tensorflow.keras.applications.resnet50 import preprocess_input


class ImageClassificationService():
    RESIZE_RESOLUTION = (128, 128)

    def __init__(self):
        self.MODEL_PATH = '.'

    def initialize_neural_network(self):
        # MOCKED
        pass

    def preprocess_image(self, numpy_image):
        print("[INFO] Preprocessing started.")
        image_array = resize(numpy_image, self.RESIZE_RESOLUTION, preserve_range=True).round(decimals=0)
        preprocessed = preprocess_input(image_array)
        return preprocessed

    def base64_to_numpy(self, b64_encoded_image):
        print("[INFO] Decoding received image.")
        imgdata = base64.b64decode(str(b64_encoded_image))
        image = Image.open(io.BytesIO(imgdata))
        return np.array(image)

    def classify_image(self, b64_encoded_image):
        print("[INFO] Classifying started.")
        image = self.base64_to_numpy(b64_encoded_image)
        image = self.preprocess_image(image)
        print(image.shape)
        # Do classification here
        pass

        # MOCKED return
        mock_response = []
        mock_response.append(ClassificationResponse(label_id=1, label_name='name1', probability=1.4))
        mock_response.append(ClassificationResponse(label_id=2, label_name='name2', probability=20.7))
        mock_response.append(ClassificationResponse(label_id=3, label_name='name3', probability=35.84))
        mock_response.append(ClassificationResponse(label_id=4, label_name='name4', probability=0.44))
        mock_response.append(ClassificationResponse(label_id=5, label_name='name5', probability=12.85))

        return mock_response
