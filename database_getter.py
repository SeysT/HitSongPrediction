import hdf5_getters as h5
import os
import pandas as pd

path = '../Data/lmd_matched_h5/'

df = pd.DataFrame()

for parent_folder in os.listdir(path):
    for sub_folder in os.listdir(path + '/' + parent_folder):
        for child_folder in os.listdir(path + '/' + parent_folder + '/' + sub_folder):
            for file in os.listdir(path + '/' + parent_folder + '/' + sub_folder + '/' + child_folder):
                ds = h5.open_h5_file_read(path + '/' + parent_folder + '/' + sub_folder + '/' + child_folder + '/' + file)

                dictionary = dict()
                dictionary['artist_terms'] = [h5.get_artist_terms(ds)]
                dictionary['artist_terms_freq'] = [h5.get_artist_terms_freq(ds)]
                dictionary['artist_terms_weight'] = [h5.get_artist_terms_weight(ds)]
                dictionary['danceability'] = [h5.get_danceability(ds)]
                dictionary['energy'] = [h5.get_energy(ds)]
                dictionary['key'] = [h5.get_key(ds)]
                dictionary['mode'] = [h5.get_mode(ds)]
                dictionary['loudness'] = [h5.get_loudness(ds)]
                dictionary['hash'] = [h5.get_audio_md5(ds)]
                dictionary['path'] = [parent_folder + '/' + sub_folder + '/' + child_folder + '/']
                dictionary['file'] = [file]

                dictionary['duration'] = [h5.get_duration(ds)]
                dictionary['artist_familiarity'] = [h5.get_artist_familiarity(ds)]
                dictionary['similar_artists'] = [h5.get_similar_artists(ds)]
                dictionary['artist_id'] = [h5.get_artist_id(ds)]
                dictionary['title'] = [h5.get_title(ds)]
                dictionary['hotttnesss'] = [h5.get_song_hotttnesss(ds)]
                dictionary['year'] = [h5.get_year(ds)]
                dictionary['latitude'] = [h5.get_artist_latitude(ds)]
                dictionary['longitude'] = [h5.get_artist_longitude(ds)]

                print(dictionary)
                df = df.append(pd.DataFrame(dictionary), ignore_index=True)
                ds.close()

print(df)
print(df.shape)
df.to_csv('test.csv', sep='\t')



