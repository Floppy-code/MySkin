import io

import numpy as np
import tensorflow as tf
import base64
from skimage.transform import resize
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input


class ImageClassificationService():
    RESIZE_RESOLUTION = (128, 128)

    def __init__(self):
        self.MODEL_PATH = '.'

    def initialize_neural_network(self):
        #MOCKED
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


