# Problem (look_at_cc): 4 points

## Question (a)
(a) Download the WARC file above, or find the copy we provide on the cluster. Let’s look at the
first page in this file. This is a gzipped file, and you can browse its contents with:

```bash 
$ zcat /data/CC/example.warc.gz | less
```

less lets you browse the file using keyboard arrows, Page Up, Page Down. To exit, press “q”.
Look at the very first web page. What is its URL? Is it still accessible? Can you tell what the
page seems to be about by looking at the raw HTML?
Deliverable: A 2-3 sentence response.

**Answer:**
It's a chinese website. I can't tell what it's about without translating it. It's url is
http://0371rykj.com/ipfhsb/34.html. It doesn't seem to be accessible. 

## Question (b)
(b) Let’s now look at the corresponding WET file:
$ zcat /data/CC/example.warc.wet.gz | less
Note that the WET files contain HTTP headers (e.g., Content-Length) that are not part of the
extracted text contents. If you look at the first example, you will see that it contains text that
was extracted from the raw HTML you just saw.
Notice that much of the extracted text is reminiscent of the HTML structure, and not actually
the page’s main content. Are there parts of the text you see that you think should have been
filtered out by the extractor? Think about the quality of this text as training data: what might
go wrong in training a model on text that looks like this? Conversely, what useful information
can a model potentially extract from this page?
Deliverable: A 3-4 sentence response.

**Answer:**

## Question (c)
(c) What makes a good training example is highly contextual. Describe an application domain for
which this example might be useful to have in the training data, and one where it might not be.
Deliverable: A 1-2 sentence response.

## Question (d)
(d) Let’s look at some more examples to get a better sense of what’s in the Common Crawl. Look
through 25 more WET records. For each record, very briefly comment on the document’s language
(if you can identify it), the domain name, what type of page it is, etc. How many examples does
it take until you see what you’d deem a “high-quality” webpage?
Deliverable: Brief annotations of 25 documents with the document’s language, domain, type of
page, and any other miscellaneous notes about the document. The number of examples it takes
until you see a high-quality example.