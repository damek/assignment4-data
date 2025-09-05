import fasttext
import os

def _model_NSFW():
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/jigsaw_fasttext_bigrams_nsfw_final.bin")):
        os.system("bash harmful_content.sh")
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/jigsaw_fasttext_bigrams_nsfw_final.bin"))

def _model_Hatespeech():
    if not os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/jigsaw_fasttext_bigrams_hatespeech_final.bin")):
        os.system("bash harmful_content.sh")
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/jigsaw_fasttext_bigrams_hatespeech_final.bin"))

# Give a persistent handle to the fasttext model
NSFW_MODEL = _model_NSFW()
HATESPEECH_MODEL = _model_Hatespeech()

def classify_nsfw(text: str):
    predicted_class, score = NSFW_MODEL.predict(text)
    return predicted_class[0].split("__label__")[1], score[0]

def classify_hatespeech(text: str):
    predicted_class, score = HATESPEECH_MODEL.predict(text)
    return predicted_class[0].split("__label__")[1], score[0]

if __name__ == "__main__":
    print(classify_nsfw("OMFG"))
    print(classify_hatespeech("This is a test"))