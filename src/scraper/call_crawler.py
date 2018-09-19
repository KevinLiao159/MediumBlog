import subprocess
import sys, os
# scrapy crawl my_scraper -o data-science.jl -a tag='data-science' -a date='2018/01/01'
def init():
    if not os.path.exists('/home/ubuntu/temp'):
        subprocess.call(["mkdir", "temp"])

if __name__ == "__main__":
    #for i in range(31):
    # subprocess.call(["cd", "mediumScraper"])
    init()
    tag = sys.argv[1]
    print("Start scraping tag {}".format(tag))

    filepath = "temp/{}.jl".format(tag)
    tag_arg = "tag={}".format(tag)
    month_days = dict({1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:30, 8:24})

    for month in range(1, 9):
        for day in range(1, month_days[month]+1):
            if  day < 10:
                day = "0" + str(day)
            else:
                day = str(day)
            print("start crawling 2018/0{month}/{day}".format(month=month, day=day))
            date_arg = "date=2018/0{month}/{day}".format(month=month, day=day)
            subprocess.call(["scrapy", "crawl", "my_scraper", "-o", filepath, "-a", tag_arg, "-a", date_arg])


    subprocess.call(["aws", "s3", "mv", filepath, "s3://mediumscraper/{}/".format(tag)])
