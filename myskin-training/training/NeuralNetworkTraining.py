import sys
import tensorflow as tf
import numpy as np
from utils.TrainingStatisticsUtils import save_training_statistics
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.layers import Input, Dense, Flatten, AveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import SparseCategoricalCrossentropy 
from sklearn.model_selection import StratifiedKFold

physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)

#===== CONSTANS =====
#Model
MODEL_NAME = 'resnet50_lr1e-4'
MODEL_ARCHITECTURE_NAME = 'resnet50'
TRAINING_STATISTICS_ACCURACY_FILE = './training/stats/network_training_acc.csv'
TRAINING_STATISTICS_VAL_ACCURACY_FILE = './training/stats/network_training_val_acc.csv'
TRAINING_STATISTICS_LOSS_FILE = './training/stats/network_training_loss.csv'
TRAINING_STATISTICS_VAL_LOSS_FILE = './training/stats/network_training_val_loss.csv'

#Dataset
FEATURE_FILE = './resources/features.npy'
LABEL_FILE = './resources/labels.npy'
PREPROCESSED_FEATURE_FILE = f'./resources/{MODEL_ARCHITECTURE_NAME}_features.npy'
PREPROCESSED_LABEL_FILE = f'./resources/{MODEL_ARCHITECTURE_NAME}_labels.npy'

fold = sys.argv[1]

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

train_indexes = []
test_indexes = []
for i, (train_index, test_index) in enumerate(skf.split(X, Y)):
    train_indexes.append(train_index)
    test_indexes.append(test_index)

train_index = train_indexes[int(fold)]
test_index = test_indexes[int(fold)]


#===== MODEL SPACE =====
print(f"===== CURRENT FOLD: {fold} =====")

earlyStopping = EarlyStopping(monitor='val_loss',
                              patience=5,)

model = Sequential()
resnet = ResNet50(include_top=False,
                  input_shape=(200, 200, 3),
                  weights='imagenet')
resnet.trainable = False
model.add(resnet)
model.add(AveragePooling2D((7, 7)))
model.add(Flatten())
model.add(Dense(7, activation = 'softmax'))

model.compile(optimizer=Adam(learning_rate=1e-4),
              loss=SparseCategoricalCrossentropy(),
              metrics=['accuracy'])

model.summary()

history = model.fit(X[train_index], Y[train_index],
                    class_weight=class_weights,
                    epochs=150,
                    batch_size=96,
                    validation_data=(X[test_index], Y[test_index]),
                    callbacks=[earlyStopping])

save_training_statistics(TRAINING_STATISTICS_ACCURACY_FILE, history.history['accuracy'], MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_LOSS_FILE, history.history['loss'], MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_VAL_ACCURACY_FILE, history.history['val_accuracy'], MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_VAL_LOSS_FILE, history.history['val_loss'], MODEL_NAME, fold)
#===== MODEL SPACE =====