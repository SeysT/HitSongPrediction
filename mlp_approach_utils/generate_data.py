import pandas as pd
import hdf5_getters as h5

import os

from csv import writer
from json import load

from utils import get_midi_name_from_matched


path = './Data/lmd_matched_h5/'
with open('./Data/match_scores.json', 'r') as json_file:
    matched_scores = load(json_file)

with open('./test.csv', 'w', newline='\n') as csv_file:
    csv_writer = writer(csv_file, delimiter=',', quotechar='|')

    csv_writer.writerow([
        'artist_terms',
        'artist_terms_freq',
        'artist_terms',
        'artist_terms_freq',
        'artist_terms_weight',
        'danceability',
        'energy',
        'key',
        'mode',
        'loudness',
        'path',
        'file',
        'duration',
        'artist_familiarity',
        'similar_artists',
        'artist_id',
        'title',
        'hotttnesss',
        'year',
        'latitude',
        'longitude',
        'midi_name'
    ])

    i = 0

    for parent_folder in os.listdir(path):
        for sub_folder in os.listdir(path + '/' + parent_folder):
            for child_folder in os.listdir(path + '/' + parent_folder + '/' + sub_folder):
                for file in os.listdir(path + '/' + parent_folder + '/' + sub_folder + '/' + child_folder):
                    with h5.open_h5_file_read(path + '/' + parent_folder + '/' + sub_folder + '/' + child_folder + '/' + file) as ds:

                        row = []
                        row += [h5.get_artist_terms(ds)]
                        row += [h5.get_artist_terms_freq(ds)]
                        row += [h5.get_artist_terms_weight(ds)]
                        row += [h5.get_danceability(ds)]
                        row += [h5.get_energy(ds)]
                        row += [h5.get_key(ds)]
                        row += [h5.get_mode(ds)]
                        row += [h5.get_loudness(ds)]
                        row += [parent_folder + '/' + sub_folder + '/' + child_folder + '/']
                        row += [file]

                        row += [h5.get_duration(ds)]
                        row += [h5.get_artist_familiarity(ds)]
                        row += [h5.get_similar_artists(ds)]
                        row += [h5.get_artist_id(ds)]
                        row += [h5.get_title(ds)]
                        row += [h5.get_song_hotttnesss(ds)]
                        row += [h5.get_year(ds)]
                        row += [h5.get_artist_latitude(ds)]
                        row += [h5.get_artist_longitude(ds)]
                        row += [get_midi_name_from_matched(file[:-3], matched_scores)]

                        ds.close()

                        csv_writer.writerow(row)

                        print(f'Row {i} written!')
                        i += 1