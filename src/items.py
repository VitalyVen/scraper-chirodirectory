import scrapy
from scrapy.loader.processors import Join


class ChirodirectoryItem(scrapy.Item):
    info = scrapy.Field(output_processor=Join())
    title = scrapy.Field()
    mail = scrapy.Field()
    site = scrapy.Field()
