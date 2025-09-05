from fastwarc.warc import ArchiveIterator, WarcRecordType
from resiliparse.parse.encoding import detect_encoding, bytes_to_str
from resiliparse.extract.html2text import extract_plain_text
import os

def extract_text_from_html_bytes(html_bytes: bytes) -> str:
    if not html_bytes:
        return ""
    
    # detect encoding
    try:
        enc = detect_encoding(html_bytes, from_html_meta=True)
    except Exception:
        enc = "utf-8"

    #  Decode 
    try:
        html_str = bytes_to_str(html_bytes, encoding=enc, errors="ignore")
    except Exception:
        # absolute last resort
        html_str = html_bytes.decode("utf-8", errors="ignore")
    
    # extract text
    return extract_plain_text(html_str)

def extract_warc_file(warc_file: str, nb_of_entries: int = 1) -> str:
    # use fastwarc to first entry of warc file, extract text from html, and then return a list of entries
    text = []
    with open(warc_file, "rb") as f:
        for record in ArchiveIterator(f, record_types=WarcRecordType.response):
        # Read the record's payload (content)
            payload = record.reader.read()
            text.append(extract_text_from_html_bytes(payload))
            if len(text) == nb_of_entries:
                break
    return text
        # Process the payload as needed

def hard_coded_extract_warc_file():
    warc_file = "data/CC/example.warc.gz"
    text = extract_warc_file(warc_file, 10)
    print(text)

if __name__ == "__main__":
    # if data/CC/example.warc.gz does not exist, run the following command
    if not os.path.exists("data/CC/example.warc.gz"):
        os.system("bash look_at_cc.sh")
    hard_coded_extract_warc_file()