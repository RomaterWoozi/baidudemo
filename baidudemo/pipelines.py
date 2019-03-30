# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from baidudemo.items import BaiduImageItem
from baidudemo.items import BaiduItem


class BaidudemoPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BaiduImageItem):
            return item
        elif isinstance(item, BaiduItem):
            return item
        pass
