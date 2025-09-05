from fastwarc.warc import ArchiveIterator, WarcRecordType
from resiliparse.parse.encoding import detect_encoding, bytes_to_str
from resiliparse.extract.html2text import extract_plain_text

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