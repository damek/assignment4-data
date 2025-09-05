## Make sure you run bash language_identification.sh to download the model first.
import fasttext
import os
import random
import cs336_data.extract_text as extract_text
from fastwarc.warc import ArchiveIterator, WarcRecordType

def _model():
    # need to give the path relative to this script
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/lid.176.bin"))

def identify_language_str(text: str):

    # I don't know why we're splitting across multiplines, I think the model cares. Probably just remove those 
    text = text.replace("\n", " ")
    predicted_language, score = _model().predict(text)
    print(predicted_language, score)
    return predicted_language[0].split("__label__")[1], score[0]

def identify_language_file(file: str) -> str:
    with open(file, "rb") as f:
        return _model().predict(f.read())

def extract_warc_and_detect_langauge(file: str, nb_entries: int = 20) -> list[str]:
    languages = []
    texts = []    
    # get path
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/CC/example.warc.gz")
    if not os.path.exists(file):
        os.system("bash look_at_cc.sh")
    if not os.path.exists("models/lid.176.bin"):
        os.system("bash language_identification.sh")
    # We're going to pick 20 entries at random from the first 1000 entries 
    entries = random.sample(range(1000), nb_entries)
    with open(file, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            if i in entries:
                text = extract_text.extract_text_from_html_bytes(record.reader.read())
                languages.append(identify_language_str(text))
                texts.append(text)
            if len(texts) == nb_entries:
                break
    return languages, texts

if __name__ == "__main__":

    languages, texts = extract_warc_and_detect_langauge(20)
    for l,text in zip(languages, texts):
        print("--------------------------------")
        print("LANGUAGE: ", l[0], "SCORE: ", l[1])
        print("text: ", text)
        print("--------------------------------")

    # now let's write these to outputs/language_identification.txt
    with open("outputs/language_identification.txt", "w") as f:
        for l,text in zip(languages, texts):
            f.write("--------------------------------\n")
            f.write("LANGUAGE: " + l[0] + " SCORE: " + str(l[1]) + "\n")
            f.write("text: " + text + "\n")
            f.write("--------------------------------\n")
    # now for each lsample and language 
    # print(identify_language_bytes("Hello, world!"))