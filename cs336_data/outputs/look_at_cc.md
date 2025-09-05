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
```bash
$ zcat /data/CC/example.warc.wet.gz | less
```
Note that the WET files contain HTTP headers (e.g., Content-Length) that are not part of the
extracted text contents. If you look at the first example, you will see that it contains text that
was extracted from the raw HTML you just saw.

Notice that much of the extracted text is reminiscent of the HTML structure, and not actually
the page’s main content. Are there parts of the text you see that you think should have been
filtered out by the extractor? Think about the quality of this text as training data: what might
go wrong in training a model on text that looks like this? Conversely, what useful information
can a model potentially extract from this page?
Deliverable: A 3-4 sentence response.

**Answer:** Contrary to what is written, most of the html has been removed. The website would probably not be great training data because it consists of things like product dimensions. I can't read the prose (it's in chinese) so i'm not sure.


## Question (c)
(c) What makes a good training example is highly contextual. Describe an application domain for
which this example might be useful to have in the training data, and one where it might not be.
Deliverable: A 1-2 sentence response.

**Answer:** It would be useful for training a model to output fake product pages. It wouldn't be useful for literature.


## Question (d)
(d) Let’s look at some more examples to get a better sense of what’s in the Common Crawl. Look
through 25 more WET records. For each record, very briefly comment on the document’s language
(if you can identify it), the domain name, what type of page it is, etc. How many examples does
it take until you see what you’d deem a “high-quality” webpage?
Deliverable: Brief annotations of 25 documents with the document’s language, domain, type of
page, and any other miscellaneous notes about the document. The number of examples it takes
until you see a high-quality example.

**Answer:**
1. Chinese, http://0371rykj.com, type: product page
2. English, http://13.usnccm.org/, type: conference webpage
3. Chinese, http://176.utchat888.com/index.phtml?PUT=gift_send&AID=220083&FID=632054, type: product page
4. Chinese, http://176766.cn/Article-3806781.html, type: product page
5. Chinese, http://178mh.com/html/,detail/,newsmovie/,wd/moAGt5YrbE/po7oqy.html,/, type: not sure.
6. Chinese, http://18sex.v340.info/?&R2=&P=11&OP=&CHANNEL=, type: ipods
7. Dutch, http://1kb.klimtoren.be/2016/06/blog-post_30.html, type: social media
8. Greek, http://1pekesat-exae.mysch.gr/exae/search.php?sid=c7c6170adb93afd9c9d00950dd818d3d, type: forum instruction page.
9. Greek, http://1pekesat-exae.mysch.gr/exae/ucp.php?mode=login&redirect=ucp.php%3Fmode%3Ddelete_cookies&sid=895ec649188d0e4bfff2f75f02ff8b0a, type: forum instruction page
10. Chinese, http://1s6605084.yhxzseo.com/?yibinnvfdkcl857593, pc online magazine.

... I could keep commenting, but, i'm just going to scroll through until i see a high-quality example.

OK this one appears to be a blog / news report. Probably the first one that looks like high quality text (though I can't read the Chinese text, so I'm unsure.)
http://3diasdemarzo.blogspot.com/2005/04/el-gobierno-no-entregar-la.html
