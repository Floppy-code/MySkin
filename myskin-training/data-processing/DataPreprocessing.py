from tensorflow.keras.applications.resnet50 import preprocess_input
#from tensorflow.keras.applications.efficientnet import preprocess_input
#from tensorflow.keras.applications.vgg19 import preprocess_input

from sklearn.preprocessing import OneHotEncoder
import numpy as np

#===== CONSTANS =====
FEATURE_FILE = '../resources/features.npy'
LABEL_FILE = '../resources/labels.npy'
MODEL_NAME = 'ResNet50_aug'
PREPROCESSED_FEATURE_FILE = f'../resources/{MODEL_NAME}_features.npy'
PREPROCESSED_LABEL_FILE = f'../resources/{MODEL_NAME}_labels.npy'

onc = OneHotEncoder(sparse_output=False)
X = np.load(open(FEATURE_FILE, 'rb'))
Y = np.load(open(LABEL_FILE, 'rb'))

X = preprocess_input(X)
Y = np.expand_dims(Y, axis=1)
Y = onc.fit_transform(Y)

print(X.shape)
print(Y.shape)

x_file = open(PREPROCESSED_FEATURE_FILE, 'wb')
y_file = open(PREPROCESSED_LABEL_FILE, 'wb')

np.save(x_file, X)
np.save(y_file, Y)

x_file.close()
y_file.close()