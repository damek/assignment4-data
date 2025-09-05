## Make sure you run bash language_identification.sh to download the model first.
import fasttext
import os

def _model():
    # need to give the path relative to this script
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/lid.176.bin"))

def identify_language_str(text: str) -> str:
    # text can include multiple lines, so we need to figure out majority languaage
    # split text into lines
    lines = text.split("\n")
    # identify language of each line
    languages = []
    for line in lines:
        predicted_language, score = _model().predict(line)
        languages.append(predicted_language[0].split("__label__")[1])
    # return majority language
    return max(set(languages), key=languages.count), 1.0   

def identify_language_file(file: str) -> str:
    with open(file, "rb") as f:
        return _model().predict(f.read())

if __name__ == "__main__":
    print(identify_language_bytes("Hello, world!"))