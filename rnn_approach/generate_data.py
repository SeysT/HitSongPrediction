import hdf5_getters as h5
import numpy as np
import os

from csv import reader, writer
from json import load

from utils import get_midi_name_from_matched
from rnn_approach.midi_to_matrix import midi_to_matrix


def generate_data(data_dirpath):
    with open(os.path.join(data_dirpath, 'match_scores.json'), 'r') as json_file:
        matched_scores = load(json_file)

    csv_content = []
    i = 0

    root_folder = os.path.join(data_dirpath, 'lmd_matched_h5')
    for parent_folder in os.listdir(root_folder):
        parent_path = os.path.join(root_folder, parent_folder)

        for sub_folder in os.listdir(parent_path):
            sub_path = os.path.join(parent_path, sub_folder)
        
            for child_folder in os.listdir(sub_path):
                child_path = os.path.join(sub_path, child_folder)
        
                for file in os.listdir(child_path):
                    with h5.open_h5_file_read(os.path.join(child_path, file)) as ds:

                        hotttnesss = h5.get_song_hotttnesss(ds)
                        if np.isnan(hotttnesss):
                            continue

                        midi_filepath = os.path.join(
                            data_dirpath,
                            'lmd_matched',
                            parent_folder,
                            sub_folder,
                            child_folder,
                            file[:-3],
                            get_midi_name_from_matched(file[:-3], matched_scores) + '.mid'
                        )

                        csv_content.append([midi_filepath, hotttnesss])
                    
                    i += 1
                    print(f'File number {i} stored in CSV content')

    csv_content = np.array(csv_content)
    np.random.shuffle(csv_content)

    print('Save train data')
    save_data_into_arrays('Data/train', csv_content[:11100])
    print('Save test data')
    save_data_into_arrays('Data/test', csv_content[11200:14300])
    print('Save validation data')
    save_data_into_arrays('Data/validation', csv_content[14400:15900])


def save_data_into_arrays(folder, data):
    i = 1
    X = []
    Y = []

    for row in data:
        X.append(midi_to_matrix(row[0]))
        Y.append(row[1])

        if i % 100 == 0:
            print(i)
            np.save(os.path.join(f'{folder}', f'/array_{i // 100}'), np.array([X, Y]))

            X = []
            Y = []
        
        i += 1


def data_generator(dirpath):
    while True:
        for file in os.listdir(dirpath):
            data = np.load(os.path.join(dirpath, file))
            X = np.array([x for x in data[0]])
            Y = data[1].astype(float)
            Y[Y > 0.8] = 1
            Y[Y <= 0.8] = 0

            yield X, Y


if __name__ == '__main__':
    generate_data('Data')