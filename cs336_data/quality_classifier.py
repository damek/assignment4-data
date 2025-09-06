import fasttext
from fastwarc.warc import ArchiveIterator, WarcRecordType
import os
import random
import cs336_data.extract_text as extract_text

def build_training_data(nb_samples: int = 1000): 
    positive_urls_warc = "data/wiki/links.sample.filtered.warc.gz"
    negative_urls_warc = "data/CC/example.warc.gz"

    total_positive_warc_entries = 0
    with open(positive_urls_warc, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            total_positive_warc_entries += 1
    total_negative_warc_entries = 0
    with open(negative_urls_warc, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            total_negative_warc_entries += 1
    ## Sample 1000 entries from positive_urls_warc and 1000 entries from negative_urls_warc
    positive_urls_warc_entries = random.sample(range(total_positive_warc_entries), nb_samples)
    negative_urls_warc_entries = random.sample(range(total_negative_warc_entries), nb_samples)
    ## Get the text from the warc files
    positive_urls_warc_text = []
    negative_urls_warc_text = []
    with open(positive_urls_warc, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            if i in positive_urls_warc_entries:
                positive_urls_warc_text.append(extract_text.extract_text_from_html_bytes(record.reader.read()))

    with open(negative_urls_warc, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            if i in negative_urls_warc_entries:
                negative_urls_warc_text.append(extract_text.extract_text_from_html_bytes(record.reader.read()))

    return positive_urls_warc_text, negative_urls_warc_text

def save_training_data(positive_urls_warc_text: list[str], negative_urls_warc_text: list[str]):
    # for each line, add __label__wiki or __label__cc
    positive_urls_warc_text = ["__label__high_quality " + text for text in positive_urls_warc_text]
    negative_urls_warc_text = ["__label__not_quality " + text for text in negative_urls_warc_text]
    # we need to add a \n to each sample then concatenate the files
    positive_urls_warc_text = "\n".join(positive_urls_warc_text)
    negative_urls_warc_text = "\n".join(negative_urls_warc_text)
    # then we just save one training data file
    training_data = positive_urls_warc_text + "\n" + negative_urls_warc_text
    with open("data/wiki/training_data.txt", "w") as f:
        f.write(training_data)
    return "data/wiki/training_data.txt"

def train_model(nb_samples: int = 1000):
    ## Build training data
    print("Building training data...")
    positive_urls_warc_text, negative_urls_warc_text = build_training_data(nb_samples)
    print("Saving training data...")
    training_data_file = save_training_data(positive_urls_warc_text, negative_urls_warc_text)
    print("Training model...")
    model = fasttext.train_supervised(input=training_data_file)
    print("Model trained...")
    model.save_model("models/wiki_quality_classifier.bin")
    return model

def classify_quality(text: str):
    return _model().predict(text)

def _model():
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/wiki_quality_classifier.bin"))

if __name__ == "__main__":
    if not os.path.exists("models/wiki_quality_classifier.bin"):
        print("No model found, training model...")
        _ = train_model(nb_samples=1000)
    else:
        print("Model found, loading model...")
    print("Model loaded...")
    print("Classifying quality...")
    print("classify_quality(sd): ", classify_quality("93480  0s"))
