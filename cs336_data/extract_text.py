from fastwarc.warc import ArchiveIterator, WarcRecordType
from resiliparse.parse.encoding import detect_encoding, bytes_to_str
from resiliparse.extract.html2text import extract_plain_text
from argparse import ArgumentParser

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
        for record in ArchiveIterator(f):
            if record.type == WarcRecordType.RESPONSE:
                text.append(extract_text_from_html_bytes(record.content))
                if len(text) == nb_of_entries:
                    break
    return text

def hard_coded_extract_warc_file():
    warc_file = "data/CC/example.warc.gz"
    text = extract_warc_file(warc_file)
    print(text)

if __name__ == "__main__":
    hard_coded_extract_warc_file()