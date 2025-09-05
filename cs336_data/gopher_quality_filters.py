import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def too_little_or_too_many_words(tokens: list[str]):
    return len(tokens) < 50 or len(tokens) > 100000

def average_word_length(tokens: list[str]):
    return sum(len(word) for word in tokens) / len(tokens) < 3

def more_than_30_percent_lines_ending_with_ellipsis(lines: list[str]):
    return sum(line.endswith("...") for line in lines) > 0.3 * len(lines)

def less_than_80_percent_words_with_at_least_one_alphabetic_character(tokens: list[str]):
    return sum(1 for word in tokens if re.search(r'[a-zA-Z]', word)) < 0.8 * len(tokens)

def gopher_quality_filter(text: str):
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    print(stop_words)
    tokens = [word for word in tokens if word not in stop_words]
    lines = text.split("\n")
    if too_little_or_too_many_words(tokens):
        return False
    if average_word_length(tokens) > 10:
        return False
    if less_than_50_non_symbol_words(tokens):
        return False
    if less_than_80_percent_words_with_at_least_one_alphabetic_character(tokens):
        return False
    return True