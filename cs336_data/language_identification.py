## Make sure you run bash language_identification.sh to download the model first.
import fasttext

def _model():
    return fasttext.load_model("models/lid.176.bin")

def identify_language(text: str) -> str:
    return _model().predict(text)

if __name__ == "__main__":
    print(identify_language("Hello, world!"))