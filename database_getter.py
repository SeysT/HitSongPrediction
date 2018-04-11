import hdf5_getters as h5
import os
import numpy as np
import pandas as pd

path = '../Data/lmd_matched_h5/A/A/'

df= pd.DataFrame()

for letter in os.listdir(path):
    for file in os.listdir(path + letter):
        ds = h5.open_h5_file_read(path + letter + '/' + file)

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


