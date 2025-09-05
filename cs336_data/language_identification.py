## Make sure you run bash language_identification.sh to download the model first.
import fasttext

def _model():
    return fasttext.load_model("models/lid.176.bin")

def identify_language_str(text: str) -> str:
    return _model().predict(text)

def identify_language_bytes(text: bytes) -> str:
    return _model().predict(text)

def identify_language_file(file: str) -> str:
    with open(file, "rb") as f:
        return _model().predict(f.read())

if __name__ == "__main__":
    print(identify_language_bytes(b"Hello, world!"))