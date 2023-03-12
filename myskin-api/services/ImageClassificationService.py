import numpy as np
import tensorflow as tf


class ImageClassificationService():

    def __init__(self):
        self.MODEL_PATH = '.'

    def initialize_neural_network(self):
        pass

    def preprocess_image(self, numpy_image):
        pass

    def base64_to_numpy(self, b64_encoded_image):
        pass

    def classify_image(self, b64_encoded_image):
        pass
