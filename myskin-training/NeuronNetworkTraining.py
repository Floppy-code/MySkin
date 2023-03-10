import tensorflow as tf
import numpy as np
import gc
from tensorflow.keras.applications import ResNet50 
from tensorflow.keras.layers import Input, Dense, Flatten
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy 
from sklearn.model_selection import StratifiedKFold
from numba import cuda

device = cuda.get_current_device()

physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)

#===== CONSTANS =====
FEATURE_FILE = './data/features.npy'
LABEL_FILE = './data/labels.npy'
MODEL_NAME = 'resnet50'
PREPROCESSED_FEATURE_FILE = f'./data/{MODEL_NAME}_features.npy'
PREPROCESSED_LABEL_FILE = f'./data/{MODEL_NAME}_labels.npy'


X = np.load(open(PREPROCESSED_FEATURE_FILE, 'rb'))
Y = np.load(open(PREPROCESSED_LABEL_FILE, 'rb'))

#Create class_weights for unbalanced dataset classes
from sklearn.utils import class_weight

class_weights = class_weight.compute_class_weight(class_weight = "balanced",
                                                  classes = np.unique(np.squeeze(Y)),
                                                  y = np.squeeze(Y))
class_weights = dict(enumerate(class_weights))

#Split into 5 folds evenly
skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)

for i, (train_index, test_index) in enumerate(skf.split(X, Y)):
    print(f"===== CURRENT FOLD: {i} =====")
    
    tf.keras.backend.clear_session()    
    #PROOF OF CONCEPT (DELETE LATER)
    model = Sequential()
    resnet = ResNet50(include_top=False, 
                      input_shape=(200, 200, 3), 
                      weights='imagenet')

    resnet.trainable = False

    model.add(resnet)
    model.add(Flatten())
    model.add(Dense(7, activation='softmax'))

    model.compile(optimizer=Adam(learning_rate=1e-3),
                  loss=SparseCategoricalCrossentropy(),
                  metrics=['accuracy'])

    model.summary()

    model.fit(X[train_index], Y[train_index],
              class_weight=class_weights,
              epochs=1, 
              batch_size=4, 
              validation_split=0.2)

    del model, resnet
    device.reset()