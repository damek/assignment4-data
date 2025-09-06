
#
# download classifier to the data/wiki_links
URL="https://nlp.stanford.edu/data/nfliu/cs336-spring-2024/assignment4/enwiki-20240420-extracted_urls.txt.gz"

mkdir -p data/wiki
[ -f data/wiki/links.txt.gz ] || wget -O data/wiki/links.txt.gz "$URL"

if [ ! -f data/wiki/links.sample.txt.gz ]; then
  gzip -cd data/wiki/links.txt.gz | shuf -n 100000 | gzip -c > data/wiki/links.sample.txt.gz
fi

# unzip the links.sample.txt.gz
gzip -cd data/wiki/links.sample.txt.gz > data/wiki/links.sample.txt

# next we'll use 
wget --timeout=5 \
-i data/wiki/links.sample.txt \
-i data/wiki/links.sample.txt \
--warc-file=data/wiki/links.sample.warc \
-O /dev/null