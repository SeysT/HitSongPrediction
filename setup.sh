#!/bin/bash

mkdir -p Data
cd Data/

wget http://hog.ee.columbia.edu/craffel/lmd/lmd_matched.tar.gz
wget http://hog.ee.columbia.edu/craffel/lmd/lmd_matched_h5.tar.gz
wget http://hog.ee.columbia.edu/craffel/lmd/match_scores.json

tar -xvf lmd_matched.tar.gz
tar -xvf lmd_matched_h5.tar.gz

rm lmd_matched.tar.gz
rm lmd_matched_h5.tar.gz

mkdir -p test
mkdir -p train
mkdir -p validation

cd ..

python generate_rnn_data.py
python generate_mlp_data.py