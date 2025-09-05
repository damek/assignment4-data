# Problem (extract_text): 3 points

Main code file: [extract_text.py](../extract_text.py)

## Question (a)

(a) Write a function that extracts text from a byte string containing raw HTML. Use
resiliparse.extract.html2text.extract_plain_text to perform the extraction. This func-
tion needs a string, so you will need to first decode the byte string into a Unicode string. Be
aware that the input byte string might not be encoded in UTF-8, so your function should be able
to detect the encoding in case UTF-8 fails. Resiliparse also offers
resiliparse.parse.encoding.detect_encoding(), which might be useful.
Deliverable: A function that takes a byte string containing HTML and returns a string con-
taining the extracted text. Implement the adapter [run_extract_text_from_html_bytes] and
make sure it passes uv run pytest -k test_extract_text_from_html_bytes

How to run: 
```bash
uv run pytest -k test_extract_text_from_html_bytes
```

## Question (b)

(b) Run your text extraction function on a single WARC file. Compare its output to the extracted
text in the corresponding WET file. What differences and/or similarities do you notice? Which
extraction seems better?
Deliverable: 2-3 sentence response comparing and contrasting the text extracted by your own
function versus the extracted text in the WET files.

**Answer:**
The extracted text appears to preserve much more of the spacial layout of the html. I suppose this could be useful. The other one seemed to remove all '\t' information.