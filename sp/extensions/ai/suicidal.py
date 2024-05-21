from googletrans import Translator
from keras.models import load_model
import pickle
from keras.preprocessing.sequence import pad_sequences

model_lstm2 = load_model(
    r'E:\ME!\learning\coding\djangoCoding_sp\sp\extensions\ai\lastm-2-layer-best_model.h5')

with open(r'E:\ME!\learning\coding\djangoCoding_sp\sp\extensions\ai\tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)


def predict_suicide_post(text):
    # Tokenize and pad the input text
    sequences = tokenizer.texts_to_sequences([text])
    padded_sequences = pad_sequences(sequences, maxlen=60, dtype='int32')

    # Predictions
    pred_lstm2 = model_lstm2.predict(padded_sequences, batch_size=1, verbose=0)

    # Choose the class with the highest probability
    result = {
        'LSTM-2 Layer': 'Potential Suicide Post' if pred_lstm2[0][0] > pred_lstm2[0][1] else 'Not Suicide Post',
    }

    return result


def translate_to_english(text):
    translator = Translator()
    translation = translator.translate(text, dest='en')
    return translation.text


def main(user_input):
    if user_input.isascii():
        prediction_result = predict_suicide_post(user_input)
    else:
        translated_input = translate_to_english(user_input)
        prediction_result = predict_suicide_post(translated_input)

    output = ''
    for model, result in prediction_result.items():
        output += f'{model}: {result}\n'
    return output


if __name__ == "__main__":
    main()
