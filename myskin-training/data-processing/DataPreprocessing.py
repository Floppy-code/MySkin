#from tensorflow.keras.applications.resnet50 import preprocess_input
from tensorflow.keras.applications.efficientnet_v2 import preprocess_input
import numpy as np

#===== CONSTANS =====
FEATURE_FILE = '../resources/features_no_augumentation.npy'
LABEL_FILE = '../resources/labels_no_augumentation.npy'
MODEL_NAME = 'EfficientNet_no_aug'
PREPROCESSED_FEATURE_FILE = f'../resources/{MODEL_NAME}_features.npy'
PREPROCESSED_LABEL_FILE = f'../resources/{MODEL_NAME}_labels.npy'

X = np.load(open(FEATURE_FILE, 'rb'))
Y = np.load(open(LABEL_FILE, 'rb'))

X = preprocess_input(X)
Y = Y.astype('float32').reshape((-1,1))

x_file = open(PREPROCESSED_FEATURE_FILE, 'wb')
y_file = open(PREPROCESSED_LABEL_FILE, 'wb')

np.save(x_file, X)
np.save(y_file, Y)

x_file.close()
y_file.close()