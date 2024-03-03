import io
from models.ClassificationResponse import ClassificationResponse
import base64
import numpy as np
from PIL import Image
from skimage.transform import resize
import tensorflow as tf
from tensorflow.keras.applications.vgg19 import preprocess_input


class ImageClassificationService():
    KERAS_MODEL_PATH = 'keras-models/vgg19_lr1e-5_final_Experiment_3/'
    RESIZE_RESOLUTION = (128, 128)
    LABEL_IDs = [0, 1, 2, 3, 4, 5, 6]
    LABEL_NAMES = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']

    def __init__(self):
        self.model = tf.saved_model.load(self.KERAS_MODEL_PATH)

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
        image = np.expand_dims(image, axis=0)

        prediction = self.model.predict(image)

        response = []
        for i in range(0, 7):
            response.append(ClassificationResponse(label_id=self.LABEL_IDs[i], label_name=self.LABEL_NAMES[i], probability=prediction[0][i]))

        return response
