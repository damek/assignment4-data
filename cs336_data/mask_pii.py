import re

_EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

def mask_emails(text: str) -> tuple[str, int]:
    return _EMAIL_RE.subn("|||EMAIL_ADDRESS|||", text or "")

# Common US phone formats: (212) 555-1212, 212-555-1212, 212.555.1212, 2125551212, +1 212 555 1212, etc.
_PHONE_RE = re.compile(r"""
(?xi)                           # verbose + case-insensitive
(?<!\w)                         # left boundary (no letter/number/_)
(?:\+?1[\s.\-]*)?               # optional country code
(?:\(?\s*\d{3}\s*\)?[\s.\-]*)   # area code, optional parentheses
(?:\d{3}[\s.\-]*)               # first three
(?:\d{4})                       # last four
(?:\s*(?:x|ext|ext\.|\#)\s*\d{1,6})?   # optional extension; NOTE: \# escaped!
(?!\w)                          # right boundary
""")

def mask_phone_numbers(text: str) -> tuple[str, int]:
    print(_PHONE_RE.subn("|||PHONE_NUMBER|||", text or ""))
    return _PHONE_RE.subn("|||PHONE_NUMBER|||", text or "")