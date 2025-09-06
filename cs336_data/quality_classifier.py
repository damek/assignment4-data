import fasttext
import fastwarc.warc import ArchiveIterator, WarcRecordType
import os


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
    positive_urls_warc_text = ["__label__wiki " + text for text in positive_urls_warc_text]
    negative_urls_warc_text = ["__label__cc " + text for text in negative_urls_warc_text]
    with open("data/wiki/positive_urls_warc_text.txt", "w") as f:
        for text in positive_urls_warc_text:
            f.write(text + "\n")
    with open("data/wiki/negative_urls_warc_text.txt", "w") as f:
        for text in negative_urls_warc_text:
            f.write(text + "\n")
    return "data/wiki/positive_urls_warc_text.txt", "data/wiki/negative_urls_warc_text.txt"

def train_model(nb_samples: int = 1000):
    ## Build training data
    positive_urls_warc_text, negative_urls_warc_text = build_training_data(nb_samples)
    positive_file, negative_file = save_training_data(positive_urls_warc_text, negative_urls_warc_text)
    model = fasttext.train_supervised(input=positive_file + " " + negative_file)
    model.save_model("models/wiki_quality_classifier.bin")
    return model

def classify_quality(text: str):
    return _model().predict(text)

def _model():
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/wiki_quality_classifier.bin"))

if __name__ == "__main__":
    train_model()
    print("classify_quality(This is a test): ", classify_quality("This is a test"))
