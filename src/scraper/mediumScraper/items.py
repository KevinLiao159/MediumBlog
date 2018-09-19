# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MediumscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    publish_time = scrapy.Field()
    url = scrapy.Field()
    author = scrapy.Field()
    author_url = scrapy.Field()
    headings = scrapy.Field()
    contents = scrapy.Field()
    mins_read = scrapy.Field()
    claps = scrapy.Field()
    lang = scrapy.Field()
    tags = scrapy.Field()
    pass
