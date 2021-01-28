# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join


class ChirodirectoryItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    info = scrapy.Field(output_processor=Join())
    title = scrapy.Field()
    mail = scrapy.Field()
    site = scrapy.Field()
