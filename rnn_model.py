# LSTM for sequence classification in the IMDB dataset
import numpy

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM, GRU, RNN
from keras.layers import Dropout

from rnn_approach_utils.generate_data import data_generator
from rnn_approach_utils.midi_to_matrix import MAX_LENGTH


def create_model(
    neurons=100,
    loss='mse',
    activation='linear',
    dropout=0.0,
    rnn_layer=LSTM,
    optimizer='adam'
):
    model = Sequential()
    model.add(rnn_layer(neurons, input_shape=(MAX_LENGTH, 53), batch_size=100))
    model.add(Dropout(dropout))
    model.add(Dense(1, activation=activation))
    model.compile(loss=loss, optimizer=optimizer, metrics=['mse'])

    return model


if __name__ == '__main__':
    with open('results.txt', 'w') as result_file:
        neurons_params = [10, 50, 100]
        dropout_params = [0.0, 0.2, 0.5]
        rnn_layer_params = [LSTM, GRU]

        for neurons in neurons_params:
            for dropout in dropout_params:
                for rnn_layer in rnn_layer_params:
                        model = create_model(
                            neurons=neurons,
                            dropout=dropout,
                            rnn_layer=rnn_layer,
                        )
                        print(model.summary())

                        model.fit_generator(data_generator('Data/train'), steps_per_epoch=110, nb_epoch=5)

                        # Final evaluation of the model
                        scores = model.evaluate_generator(data_generator('Data/test'), steps=30)
                        print(f'Neurons: {neurons}, dropout: {dropout}, rnn_layer: {rnn_layer}', file=result_file)
                        print(f'MSE: {scores[0]}', file=result_file)