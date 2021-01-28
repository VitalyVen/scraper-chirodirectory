# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from models.models import ChirodirectoryModel
from models.sessions import session


class SQLAlchemyPipeline(object):
    """Pipeline to save jokes to mysql database"""

    def close_spider(self, spider):
        session.close()

    def process_item(self, item, spider):
        obj = ChirodirectoryModel()
        obj.info = item.get("info")
        obj.title = item.get("title")
        obj.site = item.get("site")
        obj.mail = item.get("mail")
        session.add(obj)
        session.commit()
        return item
