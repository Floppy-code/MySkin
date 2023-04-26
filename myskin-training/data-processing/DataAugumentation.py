import pickle
import numpy as np
import random
from skimage.transform import resize
from skimage.util import crop
from skimage.transform import rotate
from skimage.filters import gaussian
from sklearn.preprocessing import LabelEncoder


#===== CONSTANTS =====
DATA_PATH = '../resources/loaded.pckl'
FEATURE_PATH = '../resources/features.npy'
LABEL_PATH = '../resources/labels.npy'
RESIZE_RES = (128, 128)

data = pickle.load(open(DATA_PATH, 'rb'))
data_X = []
data_y = []

for d in data:
    cropped = crop(d[0], ((0, 0), (75, 75), (0, 0)), copy=False)
    resized = resize(cropped, RESIZE_RES, preserve_range=True)
    data_X.append(np.array(resized).round(decimals=0))
    data_y.append(d[1])

data = None

#Image augumentation by rotation
to_rotate = ['bcc', 'akiec', 'vasc', 'df']
degrees_of_rotation = [90, 180, 270]

original_lenght = len(data_X)
for i in range(0, original_lenght):
    img = data_X[i]
    label = data_y[i]
    if label in to_rotate:
        for angle in degrees_of_rotation:
            data_X.append(rotate(img, angle, resize = False, preserve_range=True))
            data_y.append(label)

# Image augumentation by adding gaussian blur
to_blur_copy = ['akiec', 'mel', 'bkl', 'vasc', 'df']

blur_nv = False
blur_bcc = False
original_lenght = len(data_X)
for i in range(0, original_lenght):
    img = data_X[i]
    label = data_y[i]
    if label in to_blur_copy:
        data_X.append(gaussian(img, sigma=10, truncate=1 / 5, preserve_range=True))
        data_y.append(label)
    else:
        if (label == 'nv'):
            if (blur_nv):
                data_X[i] = gaussian(img, sigma=10, truncate=1 / 5, preserve_range=True)
            blur_nv = not blur_nv
        else:
            if (blur_bcc):
                data_X[i] = gaussian(img, sigma=10, truncate=1 / 5, preserve_range=True)
            blur_bcc = not blur_bcc

# Undersampling of nv label
indexes_to_remove = []
while len(indexes_to_remove) < (6705 - 2616):
    current = random.randrange(0, len(data_X))
    if (data_y[current] == 'nv' and current not in indexes_to_remove):
        indexes_to_remove.append(current)

indexes_to_remove.sort(reverse=True)
for i in indexes_to_remove:
    data_X.pop(i)
    data_y.pop(i)

# Encode labels and save dataset to disk
le = LabelEncoder()

data_X = np.array(data_X)
data_y = le.fit_transform(data_y)

feature_file = open(FEATURE_PATH, 'wb')
label_file = open(LABEL_PATH, 'wb')

np.save(feature_file, data_X)
np.save(label_file, data_y)

feature_file.close()
label_file.close()