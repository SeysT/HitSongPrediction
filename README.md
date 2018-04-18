Auteur : CORNET Guillaume et SEYS Thibaut

Date : 18/04/2018

# HitSongPrediction

## Installation

Pour installer le projet nous conseillons l'utilisation d'un environnement virtuel python :

```sh
virtualenv env --python=/usr/bin/python3.6
source ./env/bin/activate 
```

Pour télécharger et générer les données au bon format, nous avons écrit le script `setup.sh`. Pour le lancer :

```sh
./setup.sh
```

/!\ Les données sont volumineuses (~10 GB) donc le temps de téléchargement et de traitement est important.

## Structure du projet

Les fichiers du projet sont les suivants :

- `generate_mlp_data.py` et `generate_rnn_data.py` : script python permettant le traitement et la génération des données.
- `utils.py` et `hdf5_getters.py` : fichiers utilitaires du projet.
- `mlp_classification.ipynb` et `mlp_regresssion.ipynb` : notebooks jupyter montrant l'approche utilisée pour entraîner et évaluer les modèles liés à la prédiction de la "hotttnesss" à partir des metadonnées.
- `rnn_model.py` : script python montrant l'approche utilisée pour entraîner et évaluer les modèles liés à la prédiction de la "hotttnesss" à partir des fichiers midi.
