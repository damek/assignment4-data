# Problem (language_identification): 6 points

Main code file: [language_identification.py](../language_identification.py)

## Question (a)

(a) Write a function that will take a Unicode string and identify the main language that is present
in this string. Your function should return a pair, containing an identifier of the language and a
score between 0 and 1 representing its confidence in that prediction.
Deliverable: A function that performs language identification, giving its top language prediction
and a score. Implement the adapter [run_identify_language] and make sure it passes both
tests in uv run pytest -k test_identify_language . Note that these tests assume a particular
string identifier for English (“en”) and Chinese (“zh”), so your test adapter should perform any
applicable re-mapping, if necessary.

**Answer:** Passed

How to run: 
```bash
uv run pytest -k test_identify_language
```

## Question (b)

(b) The behavior of language models at inference time largely depends on the data they were trained
on. As a result, issues in the data filtering pipeline can result in problems downstream. What
issues do you think could arise from problems in the language identification procedure? In a
higher-stakes scenario (such as when deploying a user-facing product), how would you go about
mitigating these issues?
Deliverable: A 2-5 sentence response.

**Answer:** 
The main issue arising is that may begin displaying information in wrong language, e.g., in response to question. Mitigating: breaking documents into regions that are clearly one language, i.e., language detector has high confidence. Translating the regions to, e.g., english, and then then concatenating might be a solution to add. Asking the user which language they prefer (i know, unthinkable!).

## Question (c)

(c) Run your language identification system on text extracted from the WARC files (via your
previously-implemented text extraction function). Manually identify the language in 20 random
examples and compare your labels with the classifier predictions. Report any classifier errors.
What fraction of documents are English? Based on your observations, what would be a suitable
classifier confidence threshold to use in filtering?
Deliverable: A 2-5 sentence response.

Look at [language_identification.txt](../outputs/language_identification.txt) for the results.

Seems to be 1 error in 20. When I ran the code,
```bash
uv run language_identification.py
```
I sampled 20 random from the first 10000 examples and only 1 seemed wrong. One had mixed english and french, but the confidence was low (35%).

Proabbly 60% is ok for a threshold.
