from preprocess import read_files
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer

def token():
    y_train, train_text = read_files("train")
    y_test, test_text = read_files("test")
    token = Tokenizer(num_words=3800)
    token.fit_on_texts(train_text)

    print(token.document_count)
    #print(token.word_index)

    x_train_seq = token.texts_to_sequences(train_text)
    x_test_seq = token.texts_to_sequences(test_text)
    x_train = sequence.pad_sequences(x_train_seq, maxlen=380)
    x_test = sequence.pad_sequences(x_test_seq, maxlen=380)

    return x_train, x_test, y_train, y_test