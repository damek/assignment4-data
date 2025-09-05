import re
import os
import random
from fastwarc.warc import ArchiveIterator, WarcRecordType
from cs336_data.extract_text import extract_text_from_html_bytes

_EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

def mask_emails(text: str) -> tuple[str, int]:
    return _EMAIL_RE.subn("|||EMAIL_ADDRESS|||", text or "")

# GPT 5 no way.
_PHONE_RE = re.compile(r"""
(?<!\w)                                             # left boundary
(?! (?:\d{1,3}\.){3}\d{1,3}\b )                     # not an IPv4 address
(?! \d{4}(?:[ -]\d{4}){3}\b )                       # not a 16-digit CC pattern
(?:\+?\s*\d{1,3}[\s.\-]*)?                          # optional +country
(?:\(\s*\d{1,4}\s*\)|\d{1,4})[\s.\-]*               # area/trunk (parens ok)
(?:\d[\s.\-]*){6,12}                                # rest: 6–12 more digits
(?: (?:x|ext|ext\.|\#)\s*\d{1,6} )?                 # optional extension
(?!\w)                                              # right boundary
""", re.VERBOSE | re.IGNORECASE)

def mask_phone_numbers(text: str) -> tuple[str, int]:
    return _PHONE_RE.subn("|||PHONE_NUMBER|||", text or "")

_IPV4_RE = re.compile(r"""
(?<!\d)                                  # left boundary: not preceded by a digit
(?:                                      # 3 x (octet '.')
  (?:25[0-5]|2[0-4]\d|1\d\d|0?\d?\d)\.
){3}
(?:25[0-5]|2[0-4]\d|1\d\d|0?\d?\d)       # final octet
(?!\d)                                   # right boundary: not followed by a digit
""", re.VERBOSE)    

def mask_ips(text: str) -> tuple[str, int]:
    return _IPV4_RE.subn("|||IP_ADDRESS|||", text or "")


def extract_warc_and_mask_pii(nb_entries: int = 20) -> list[str]:
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/CC/example.warc.gz")
    if not os.path.exists(file):
        os.system("bash look_at_cc.sh")
    # We're going to pick 20 entries at random from the first 1000 entries 
    entries = random.sample(range(10000), nb_entries)
    masked_texts = []
    with open(file, "rb") as f:
        for i, record in enumerate(ArchiveIterator(f, record_types=WarcRecordType.response)):
            if i in entries:
                text = extract_text_from_html_bytes(record.reader.read())
                masked_text = mask_emails(text)[0]
                masked_text = mask_phone_numbers(masked_text)[0]
                masked_text = mask_ips(masked_text)[0]
                masked_texts.append(masked_text)
            if len(masked_texts) == nb_entries:
                break
    return masked_texts


if __name__ == "__main__":

    masked_texts = extract_warc_and_mask_pii(20)
    for text in masked_texts:
        print(text)
        print("--------------------------------")
    # now let's write these to outputs/mask_pii.txt
    with open("outputs/mask_pii.txt", "w") as f:
        for text in masked_texts:
            f.write(text + "\n")
            f.write("--------------------------------\n")