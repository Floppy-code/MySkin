import os
import pickle
import cv2
import pandas as pd

#===== CONSTANTS ======
IMAGE_FOLDER_PATH = '../resources/HAM10000_images'
IMAGE_METADATA_PATH = '../resources/HAM10000_metadata.csv'
LOADED_DATA_PATH = '../resources/loaded.pckl'

image_metadata = pd.read_csv(IMAGE_METADATA_PATH)
temp_metadata = image_metadata[['lesion_id', 'image_id', 'dx']].to_numpy()

metadata_dict = {}
for metadata in temp_metadata:
    metadata_dict[metadata[1]] = metadata[2]

loaded_data = []

counter = 1
for image_name in image_metadata['image_id'].to_numpy():
    if (counter % 100 == 0):
        print(f'\rLoading images: {counter}/{len(image_metadata)}', end='')
    counter += 1

    try:
        image_path = os.path.join(IMAGE_FOLDER_PATH, image_name) + '.jpg'
        image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        loaded_data.append((image, metadata_dict[image_name]))
    except:
        print(f'[ERROR] Image {image_name}.jpg could not be loaded!')
print('...DONE')

data_file = open(LOADED_DATA_PATH, 'wb')
pickle.dump(loaded_data, data_file)