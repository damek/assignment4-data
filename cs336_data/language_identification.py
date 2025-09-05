## Make sure you run bash language_identification.sh to download the model first.
import fasttext
import os
# import extract_text

def _model():
    # need to give the path relative to this script
    return fasttext.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)), "models/lid.176.bin"))

def identify_language_str(text: str):

    # I don't know why we're splitting across multiplines, I think the model cares. Probably just remove those 
    text = text.replace("\n", " ")
    predicted_language, score = _model().predict(text)
    print(predicted_language, score)
    return predicted_language[0].split("__label__")[1], score[0]

    # # text can include multiple lines, so we need to figure out majority languaage
    # # split text into lines
    # lines = text.split("\n")
    # # identify language of each line, choose the language with maximal total score across all lines
    # languages = []
    # scores = []
    # for line in lines:
    #     predicted_language, score = _model().predict(line)
    #     languages.append(predicted_language[0].split("__label__")[1])
    # # return majority language
    # return max(set(languages), key=languages.count), score/len(lines)   

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
    # now for each lsample and language 
    # print(identify_language_bytes("Hello, world!"))