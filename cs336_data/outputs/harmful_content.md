# Problem (harmful_content): 6 points

Main code file: [harmful_content.py](../harmful_content.py)

## Question 1

Write a function to detect NSFW content.
Deliverable: A function that labels a given string as containing NSFW content or not, returning
a pair containing both the label and a confidence score. Implement the adapter
[run_classify_nsfw] and make sure it passes
uv run pytest -k test_classify_nsfw. Note that this test is just a sanity check, taken from
the Jigsaw dataset, but by no means asserts that your classifier is accurate, which you should
validate.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_classify_nsfw
```

## Question 2

Write a function to detect toxic speech.
Deliverable: A function that labels a given string as consisting of toxic speech or not, returning
a pair containing both the label and a confidence score. Implement the adapter
[run_classify_toxic_speech] and make sure it passes
uv run pytest -k test_classify_toxic_speech. Again, this test is just a sanity check, also
taken from Jigsaw.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_classify_toxic_speech
```

## Question 3

What problems do you think might arise downstream in a language model when these filters are
applied to create the training set? How might you mitigate these issues?
Deliverable: A 2-5 sentence response.

**Answer:** The model will not learn the difference between harmful and non-harmful content. It also won't be able to interact with harmful content reliably. It might also parrot harmful content back because of this. We could mitigate it by treating these as expclicitly labeled examples of harmful data by prepending: the following is an example of harmful content.

## Question 4

Run your harmful content filters on text extracted from the WARC files (via your previously-
implemented text extraction function). Look through 20 random examples and compare the
classifier predictions to your own judgments. Report any classifier errors. What fraction of
documents are harmful? Based on your observations, what would be suitable classifier confidence
threshold(s) to use in filtering?
Deliverable: A 2-5 sentence response.

**Answer:**

There was one non toxic that included belittling language in russian (according to chatgpt). It's score was .8. I asked it to translate parts it seem there are indeed slightly toxic language. So perhaps .75 is a good for toxic and .7 is a goo threshood for nsfw.

But in my 50 random examples (of 100000), I didn't find much harmful content detected.