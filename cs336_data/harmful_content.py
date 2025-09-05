import fasttext
import os
import random
from fastwarc.warc import ArchiveIterator, WarcRecordType
import cs336_data.extract_text as extract_text

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

_PRESENCE_THRESH = 0.80

def _max_prob_for_label(model, text, positive_label: str, size: int = 1000, stride: int = 800) -> float:
    # collapse newlines like your original, then chunk
    text = text.replace("\n", " ")
    if not text:
        return 0.0
    best = 0.0
    for i in range(0, len(text), stride):
        chunk = text[i:i+size]
        # same API/vars as your code
        predicted_class, score = model.predict(chunk, k=2)
        labels = [lbl.split("__label__")[1] for lbl in predicted_class]
        for lbl, sc in zip(labels, score):
            if lbl == positive_label and float(sc) > best:
                best = float(sc)
        if i + size >= len(text):
            break
    return best

def classify_nsfw(text: str):
    # remove newlines (kept for style)
    text = text.replace("\n", " ")
    p = _max_prob_for_label(NSFW_MODEL, text, "nsfw")
    label = "nsfw" if p >= _PRESENCE_THRESH else "clean"
    return label, p

def classify_hatespeech(text: str):
    # remove newlines (kept for style)
    text = text.replace("\n", " ")
    # Try common positive label names; keep the max
    p = max(
        _max_prob_for_label(HATESPEECH_MODEL, text, "hatespeech"),
        _max_prob_for_label(HATESPEECH_MODEL, text, "toxic"),
    )
    label = "hatespeech" if p >= _PRESENCE_THRESH else "clean"
    return label, p


def extract_warc_and_detect_harmful_content(nb_entries: int = 20) -> list[str]:
    nsfw_labels = []
    hatespeech_labels = []
    texts = []    
    # get path
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/CC/example.warc.gz")
    if not os.path.exists(file):
        os.system("bash look_at_cc.sh")
    if not os.path.exists("models/jigsaw_fasttext_bigrams_hatespeech_final.bin") or not os.path.exists("models/jigsaw_fasttext_bigrams_nsfw_final.bin"):
        os.system("bash harmful_content.sh")
    # We're going to pick 20 entries at random from the first 1000 entries 
    entries = random.sample(range(100000), nb_entries)
    total_entries = 0
    with open(file, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            if i in entries:
                text = extract_text.extract_text_from_html_bytes(record.reader.read())
                nsfw_labels.append(classify_nsfw(text))
                hatespeech_labels.append(classify_hatespeech(text))
                texts.append(text)
            if len(texts) == nb_entries:
                break
            total_entries += 1
    print("Total entries: ", total_entries)
    return nsfw_labels, hatespeech_labels, texts
if __name__ == "__main__":

    # first print then save to outputs/harmful_content.txt
    nsfw_labels, hatespeech_labels, texts = extract_warc_and_detect_harmful_content(50)
    for nsfw_label, hatespeech_label, text in zip(nsfw_labels, hatespeech_labels, texts):
        print("--------------------------------")
        print("NSFW LABEL: ", nsfw_label[0], "SCORE: ", nsfw_label[1], "HATESPEECH LABEL: ", hatespeech_label[0], "SCORE: ", hatespeech_label[1])
        print("text: ", text)
        print("--------------------------------")
    with open("outputs/harmful_content.txt", "w") as f:
        for nsfw_label, hatespeech_label, text in zip(nsfw_labels, hatespeech_labels, texts):
            f.write("--------------------------------\n")
            f.write("NSFW LABEL: " + nsfw_label[0] + " SCORE: " + str(nsfw_label[1]) + " HATESPEECH LABEL: " + hatespeech_label[0] + " SCORE: " + str(hatespeech_label[1]) + "\n")
            f.write("text: " + text + "\n")
            f.write("--------------------------------\n")