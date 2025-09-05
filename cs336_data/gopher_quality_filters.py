import nltk
from nltk.tokenize import word_tokenize
import re
import os
import random
from fastwarc.warc import ArchiveIterator, WarcRecordType
import cs336_data.extract_text as extract_text

def is_too_little_or_too_many_words(tokens: list[str]):
    return len(tokens) < 50 or len(tokens) > 100000

def is_average_word_length_less_than_3(tokens: list[str]):
    return (sum(len(word) for word in tokens) / len(tokens)) < 3

def is_average_word_length_greater_than_10(tokens: list[str]):
    return (sum(len(word) for word in tokens) / len(tokens)) > 10

def is_more_than_30_percent_lines_ending_with_ellipsis(lines: list[str]):
    return sum(line.endswith("...") for line in lines) > 0.3 * len(lines)
    
def is_less_than_80_percent_words_with_at_least_one_alphabetic_character(tokens: list[str]):
    return sum(1 for word in tokens if re.search(r'[a-zA-Z]', word)) < 0.8 * len(tokens)

def gopher_quality_filter(text: str):
    tokens = word_tokenize(text)
    lines = text.split("\n")
    if is_too_little_or_too_many_words(tokens):
        return False
    if is_average_word_length_less_than_3(tokens):
        return False
    if is_average_word_length_greater_than_10(tokens):
        return False
    if is_more_than_30_percent_lines_ending_with_ellipsis(lines):
        return False
    if is_less_than_80_percent_words_with_at_least_one_alphabetic_character(tokens):
        return False
    return True


def extract_warc_and_gopher_quality_filter(nb_entries: int = 20) -> list[str]:
    labels = []
    texts = []    
    # get path
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/CC/example.warc.gz")
    if not os.path.exists(file):
        os.system("bash look_at_cc.sh")
    # We're going to pick 20 entries at random from the first 100000 entries 
    entries = random.sample(range(100000), nb_entries)
    total_entries = 0
    with open(file, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            if i in entries:
                text = extract_text.extract_text_from_html_bytes(record.reader.read())
                labels.append(gopher_quality_filter(text))
                texts.append(text)
            if len(texts) == nb_entries:
                break
            total_entries += 1
    print("Total entries: ", total_entries)
    return labels, texts


if __name__ == "__main__":

    labels, texts = extract_warc_and_gopher_quality_filter(50)
    for label, text in zip(labels, texts):
        print("--------------------------------")
        print("LABEL: ", label)
        print("text: ", text)
        print("--------------------------------")
    with open("outputs/gopher_quality_filter.txt", "w") as f:
        for label, text in zip(labels, texts):
            f.write("--------------------------------\n")
            f.write("LABEL: " + str(label) + "\n")
            f.write("text: " + text + "\n")
            f.write("--------------------------------\n")