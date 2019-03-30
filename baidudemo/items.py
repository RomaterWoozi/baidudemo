# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BaiduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    new_event_index = scrapy.Field()
    new_event_name = scrapy.Field()
    new_event_link = scrapy.Field()
    pass


class BaiduImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    pass
