# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import re
# import pymongo
from scrapy.conf import settings
from scrapy.exceptions import DropItem

class PreprocessPipeline(object):

    def process_item(self, item, spider):
        cols = ['title', 'author', 'url', 'author_url', 'contents', 'publish_time', 'mins_read', 'claps', 'headings', 'lang']
        for col in cols:
            if len(item[col]) == 0:
                item[col] = ""
            elif len(item[col]) == 1:
                item[col] = item[col][0]
            else:
                item[col] = ";".join(item[col])

        ## filter out posts that were not written in English
        if item['lang'] != 'en':
            raise DropItem("Not written in English")

        if item['mins_read']:
            item['mins_read'] = re.findall(r'[0-9]+', item['mins_read'])[0]
        if item['publish_time']:
            item['publish_time'] = datetime.datetime.strptime(item['publish_time'][:10], "%Y-%m-%d")

        if item['claps']:
            # '2.9K'
            if item['claps'][-1] == 'K':
                temp = item['claps'].strip('K').split('.')
                if len(temp) == 1:
                    item['claps'] = int(temp[0]) * 1000
                else:
                    item['claps'] = int(temp[0]) * 1000 + int(temp[1]) * 100
            else:
                item['claps'] = int(item['claps'])
        else:
            item['claps'] = 0
        return item



class MongDBPipeline(object):

    def __init__(self):
        self.mongodb_server = settings['MONGODB_SERVER']
        self.mongodb_port = settings['MONGODB_PORT']
        self.mongo_db = settings['MONGODB_DB']

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongodb_server, self.mongodb_port)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        self.db[item['tag']].insert_one(dict(item))
        return item
