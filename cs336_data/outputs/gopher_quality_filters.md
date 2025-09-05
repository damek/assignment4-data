# Problem (gopher_quality_filters): 3 points

Main code file: [gopher_quality_filters.py](../gopher_quality_filters.py)

## Question (a)

Implement (at least) the subset of the Gopher quality filters as described above. For tokenizing
text into words, you might find the NLTK package useful (specifically nltk.word_tokenize),
though you’re not required to use it.
Deliverable: A function that takes a string as its only argument and returns a boolean indi-
cating whether the text passes the Gopher quality filters. Implement the adapter
[run_gopher_quality_filter]. Then, make sure your filters pass the tests in uv run pytest
-k test_gopher.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_gopher
```

## Question (b)

Run your rule-based quality filter on text extracted from the WARC files (via your previously-
implemented text extraction function). Look through 20 random examples and compare the filter
predictions to your own judgment. Comment on any cases where the quality filters differ from
your judgments.
Deliverable: A 2-5 sentence response.

**Answer:** 9/50 examples were classified as gopher quality. 

Surprisingly all the examples looked like they were classified correctly.