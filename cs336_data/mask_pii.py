import re

_EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

def mask_emails(text: str) -> tuple[str, int]:
    return _EMAIL_RE.subn("|||EMAIL_ADDRESS|||", text or "")

# GPT 5 no way.
_PHONE_RE = re.compile(r"(?xi)(?<!\w)(?:\+?1[\s.\-]*)?(?:\(?\s*\d{3}\s*\)?[\s.\-]*)(?:\d{3}[\s.\-]*)(?:\d{4})(?:\s*(?:x|ext|ext\.|\#)\s*\d{1,6})?(?!\w)")

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