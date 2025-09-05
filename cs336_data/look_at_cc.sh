# Download WARC and WET files to cs336_data/assets
# name them example.warc.gz and example.warc.wet.gz

mkdir -p cs336_data/assets
cd cs336_data/assets    
wget https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-18/segments/1744889135610.12/
warc/CC-MAIN-20250417135010-20250417165010-00065.warc.gz
mv warc/CC-MAIN-20250417135010-20250417165010-00065.warc.gz example.warc.gz
wget https://data.commoncrawl.org/crawl-data/CC-MAIN-2025-18/segments/1744889135610.12/
wet/CC-MAIN-20250417135010-20250417165010-00065.warc.wet.gz
mv wet/CC-MAIN-20250417135010-20250417165010-00065.warc.wet.gz example.warc.wet.gz