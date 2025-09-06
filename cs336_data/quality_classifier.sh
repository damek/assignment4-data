

# download classifier to the data/wiki_links

mkdir -p data
[ -f data/wiki_links.txt.gz ] || wget -O data/wiki_links.txt.gz "$URL"

if [ ! -f data/wiki_links.sample.txt.gz ]; then
  gzip -cd data/wiki_links.txt.gz | shuf -n 100000 | gzip -c > data/wiki_links.sample.txt.gz
fi