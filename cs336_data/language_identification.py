## Make sure you run bash language_identification.sh to download the model first.
import fasttext

def _model():
    return fasttext.load_model("models/lid.176.bin")

def identify_language_str(text: str) -> str:
    predicted_language, score = _model().predict(text)
    print(predicted_language, score)
    return predicted_language[0], score[0]

def identify_language_file(file: str) -> str:
    with open(file, "rb") as f:
        return _model().predict(f.read())

if __name__ == "__main__":
    print(identify_language_bytes("Hello, world!"))