sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev
pip install scrapy
pip install fake-useragent
echo "nohup python call_crawler.py '$1' >> output.txt 2>> stderr.txt &"
nohup python call_crawler.py $1 >> output.txt 2>> stderr.txt &