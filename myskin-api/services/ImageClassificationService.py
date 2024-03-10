import io
from models.ClassificationResponse import ClassificationResponse
import base64
import numpy as np
from PIL import Image
from skimage.transform import resize
import tensorflow as tf
from tensorflow.keras.applications.vgg19 import preprocess_input

# Wrapper added so we can load Keras models saved using no longer compatible version of protobuf
class CustomModelLayer(tf.keras.layers.Layer):
    def __init__(self, model, **kwargs):
        super(CustomModelLayer, self).__init__(**kwargs)
        self.model = model

    def build(self, input_shape):
        # Explicitly create variables using add_weight
        self._trainable_weights.extend(self.model.trainable_variables)

    def call(self, inputs, **kwargs):
        return self.model(inputs)


class ImageClassificationService():
    KERAS_MODEL_PATH = 'keras-models/vgg19_lr1e-5_final_Experiment_3/'
    RESIZE_RESOLUTION = (128, 128)
    LABEL_IDs = [0, 1, 2, 3, 4, 5, 6]
    LABEL_NAMES = ['akiec', 'bcc', 'bkl', 'df', 'mel', 'nv', 'vasc']

    def __init__(self):
        self.load_model()

    def load_model(self):
        tf_model = tf.saved_model.load(self.KERAS_MODEL_PATH)

        input_layer = tf.keras.layers.Input(shape=(128, 128, 3))
        output_layer = CustomModelLayer(tf_model)(input_layer)

        self.model = tf.keras.Model(inputs=input_layer, outputs=output_layer)

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
