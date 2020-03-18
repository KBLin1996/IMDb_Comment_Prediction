from download import comment
from token_create import token
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM

def model():
    model = Sequential()
    model.add(Embedding(output_dim=32,
                    input_dim=3800,
                    input_length=380))
    model.add(Dropout(0.2))

    model.add(LSTM(32))
    model.add(Dense(units=256,
                    activation='relu'))
    model.add(Dropout(0.2))

    model.add(Dense(units=1,
                    activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])

    return model

if __name__ == '__main__':
    comment()
    x_train, x_test, y_train, y_test = token()
    Model = model()
    train_history = Model.fit(x_train, y_train, batch_size=100, epochs=15, verbose=2, validation_split=0.2)
    score = Model.evaluate(x_test, y_test, verbose=1)
    print(score[1])