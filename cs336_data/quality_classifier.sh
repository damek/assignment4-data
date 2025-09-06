
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

URLS="data/wiki/links.sample.txt"
WBASE="data/wiki/links.sample"   # same folder as your list

wget --no-verbose \
  --tries=1 \
  --timeout=5 --dns-timeout=5 --connect-timeout=5 --read-timeout=5 \
  --max-redirect=5 \
  --no-hsts \
  --warc-file="$WBASE" --warc-cdx --warc-compression=gzip \
  -i "$URLS" \
  -O /dev/null
