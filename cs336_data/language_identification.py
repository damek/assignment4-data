## Make sure you run bash language_identification.sh to download the model first.
import fasttext
import os

def _model():
    # need to give the path relative to this script
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/lid.176.bin"))

def identify_language_str(text: str) -> str:
    predicted_language, score = _model().predict(text)
    # extract language from predicted_language
    predicted_language = predicted_language[0].split("__label__")[1]
    print(predicted_language, score)
    return predicted_language[0], score[0]

def identify_language_file(file: str) -> str:
    with open(file, "rb") as f:
        return _model().predict(f.read())

if __name__ == "__main__":
    print(identify_language_bytes("Hello, world!"))