import sys
import tensorflow as tf
import numpy as np
from utils.TrainingStatisticsUtils import save_training_statistics
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.applications import EfficientNetB3
from tensorflow.keras.layers import Input, Dense, Flatten, AveragePooling2D
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import recall_score, precision_score

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

fold = sys.argv[1]
lr_str = '1e-' + sys.argv[2]
lr_float = float(lr_str)

# ===== CONSTANS =====
# Model
MODEL_NAME = 'EfficientNetB3_lr' + lr_str + '_final'
MODEL_ARCHITECTURE_NAME = 'EfficientNet_aug'
TRAINING_STATISTICS_ACCURACY_FILE = './training/stats/network_training_acc.csv'
TRAINING_STATISTICS_VAL_ACCURACY_FILE = './training/stats/network_training_val_acc.csv'
TRAINING_STATISTICS_VAL_PRECISION_FILE = './training/stats/network_training_val_prec.csv'
TRAINING_STATISTICS_VAL_RECALL_FILE = './training/stats/network_training_val_rec.csv'
TRAINING_STATISTICS_LOSS_FILE = './training/stats/network_training_loss.csv'
TRAINING_STATISTICS_VAL_LOSS_FILE = './training/stats/network_training_val_loss.csv'
MODEL_SAVE_PATH = f'./training/models/{MODEL_NAME}'

# Dataset
FEATURE_FILE = './resources/features.npy'
LABEL_FILE = './resources/labels.npy'
PREPROCESSED_FEATURE_FILE = f'./resources/{MODEL_ARCHITECTURE_NAME}_features.npy'
PREPROCESSED_LABEL_FILE = f'./resources/{MODEL_ARCHITECTURE_NAME}_labels.npy'

X = np.load(open(PREPROCESSED_FEATURE_FILE, 'rb'))
Y = np.load(open(PREPROCESSED_LABEL_FILE, 'rb'))

# Create class_weights for unbalanced dataset classes
from sklearn.utils import class_weight

y_integers = np.argmax(Y, axis=1)
class_weights = class_weight.compute_class_weight(class_weight="balanced",
                                                  classes=np.unique(y_integers),
                                                  y=y_integers)
class_weights = dict(enumerate(class_weights))

# Split into 5 folds evenly
skf = StratifiedKFold(n_splits=5, random_state=None, shuffle=False)

train_indexes = []
test_indexes = []
for i, (train_index, test_index) in enumerate(skf.split(X, y_integers)):
    train_indexes.append(train_index)
    test_indexes.append(test_index)

train_index = train_indexes[int(fold)]
test_index = test_indexes[int(fold)]

# ===== MODEL SPACE =====
print(f"===== CURRENT FOLD: {fold} =====")

earlyStopping = EarlyStopping(monitor='val_loss',
                              patience=15,)

model = Sequential()
efficient_net_b3 = EfficientNetB3(include_top=False,
                                  input_shape=(128, 128, 3),
                                  weights='imagenet',
                                  pooling='avg')
#efficient_net_b4.trainable = True

for l in efficient_net_b3.layers:
    if 'block7' in l.name:
        l.trainable = True
    else:
        l.trainable = False


model.add(efficient_net_b3)
model.add(Dense(7, activation='softmax'))

model.compile(optimizer=Adam(learning_rate=lr_float),
              loss=CategoricalCrossentropy(),
              metrics=['accuracy'])

model.summary(expand_nested=True)

history = model.fit(X[train_index], Y[train_index],
                    class_weight=class_weights,
                    epochs=200,
                    batch_size=64,
                    validation_data=(X[test_index], Y[test_index]),
                    callbacks=[earlyStopping])

y_true = np.argmax(Y[test_index], axis = 1)
y_pred = np.argmax(model.predict(X[test_index]), axis = 1)

recall = [recall_score(y_true, y_pred, average='macro')]
precision = [precision_score(y_true, y_pred, average='macro')]

#model.save(MODEL_SAVE_PATH)
save_training_statistics(TRAINING_STATISTICS_ACCURACY_FILE, history.history['accuracy'], MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_LOSS_FILE, history.history['loss'], MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_VAL_ACCURACY_FILE, history.history['val_accuracy'], MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_VAL_LOSS_FILE, history.history['val_loss'], MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_VAL_PRECISION_FILE, precision, MODEL_NAME, fold)
save_training_statistics(TRAINING_STATISTICS_VAL_RECALL_FILE, recall, MODEL_NAME, fold)
#===== MODEL SPACE =====
