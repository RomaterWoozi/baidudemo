# -*- coding: utf-8 -*-
import scrapy

from baidudemo.items import BaiduItem
from baidudemo.items import BaiduImageItem


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['top.baidu.com', 'image.baidu.com']
    b = 1
    fr = 20811
    url = 'http://top.baidu.com/buzz?b=%d&fr=%d' % (b, fr)

    start_urls = [url, " http://image.baidu.com/search/index"]

    # def parse(self, response):
    #     for each in response.xpath("//tr[@class='even']|//tr[@class='odd']"):
    #         item = BaiduItem()
    #         item['positionname'] = each.xpath("./td[1]/a/text()").extract()[0]
    #         item['positionlink'] = each.xpath("./td[1]/a/@href").extract()[0]
    #         try:
    #             item['positionType'] = each.xpath("./td[2]/text()").extract()[0]
    #         except IndexError:
    #             pass
    #         item['peopleNum'] = each.xpath("./td[3]/text()").extract()[0]
    #         item['workLocation'] = each.xpath("./td[4]/text()").extract()[0]
    #         item['publishTime'] = each.xpath("./td[5]/text()").extract()[0]
    #         yield item
    #
    #     pass
    def parse(self, response):
        index = 0
        # newevent_list=[]
        for each in response.xpath("//tr[@class='hideline']|//tr[not(@class='item-tr')]"):
            index = index + 1
            if (index == 1):
                continue
            item = BaiduItem()
            item['new_event_index'] = each.xpath("./td[1]/span/text()").extract()[0]
            item['new_event_name'] = each.xpath("./td[2]/a/text()").extract()[0]
            item['new_event_link'] = each.xpath("./td[3]/a[3]/@href").extract()[0]
            # newevent_list.append(item)
            yield item
            yield scrapy.Request(item['new_event_link'], callback=self.parse_page1)

        pass

    def parse_page1(self, response):
        print(response.url)
        image_item = BaiduImageItem()
        images_list = []
        # for each in response.xpath("//div[@class='imgbox']"):
        # images_list.append(each.xpath("./a/img/@src").extract()[0])
        for temp in response.xpath("//div[@class='topInfoBar']"):
            print(temp.extract())

        image_item['image_urls'] = images_list
        yield image_item
        pass
