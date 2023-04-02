import os.path
import keras.backend as K


def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)), axis=0)
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)), axis=0)
    recall = true_positives / (possible_positives + K.epsilon())
    recall = K.mean(recall)
    return recall


def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)), axis=0)
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)), axis=0)
    precision = true_positives / (predicted_positives + K.epsilon())
    precision = K.mean(precision)
    return precision


def save_training_statistics(file_path, data_to_save, model_name, model_fold):
    save_file = open(file_path, 'a+')
    save_file.write(model_name + ' fold_{}'.format(model_fold))
    for value in data_to_save:
        save_file.write(';{}'.format(value))
    save_file.write('\n')
    save_file.close()