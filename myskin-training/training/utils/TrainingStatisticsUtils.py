import os.path


def save_training_statistics(file_path, data_to_save, model_name, model_fold):
    save_file = open(file_path, 'a+')
    save_file.write(model_name + ' fold_{}'.format(model_fold))
    for value in data_to_save:
        save_file.write(';{}'.format(value))
    save_file.write('\n')
    save_file.close()