import re

_EMAIL_RE = re.compile(r"(?i)\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b")

def mask_emails(text: str) -> tuple[str, int]:
    return _EMAIL_RE.subn("|||EMAIL_ADDRESS|||", text or "")

# adapter for tests
def run_mask_emails(text: str) -> tuple[str, int]:
    return mask_emails(text)