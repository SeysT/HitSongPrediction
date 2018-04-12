import hdf5_getters as h5
import os
import numpy as np
import pandas as pd

path = '../Data/lmd_matched_h5/'

df= pd.DataFrame()

for parent_folder in os.listdir(path):
    for sub_folder in os.listdir(path + '/' + parent_folder):
        for child_folder in os.listdir(path + '/' + parent_folder + '/' + sub_folder):
            for file in os.listdir(path + '/' + parent_folder + '/' + sub_folder + '/' + child_folder):
                ds = h5.open_h5_file_read(path + '/' + parent_folder + '/' + sub_folder + '/' + child_folder + '/' + file)

                dictionary = dict()
                dictionary['duration'] = [h5.get_duration(ds)]
                dictionary['num_songs'] = [h5.get_num_songs(ds)]
                dictionary['artist_familiarity'] = [h5.get_artist_familiarity(ds)]
                dictionary['artist'] = [h5.get_artist_name(ds)]
                dictionary['title'] = [h5.get_title(ds)]
                dictionary['hotttnesss'] = [h5.get_song_hotttnesss(ds)]

                print(dictionary)
                df = df.append(pd.DataFrame(dictionary), ignore_index=True)
                ds.close()

print(df)
print(df.shape)
df.to_csv('test.csv', sep='\t')



