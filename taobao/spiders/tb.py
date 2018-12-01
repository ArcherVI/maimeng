# -*- coding: utf-8 -*-
import scrapy

from taobao.items import TaobaoItem


class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['www.meng2u.com']
    start_urls = ['http://www.meng2u.com/allshow/']

    def parse(self, response):
        for each in response.xpath("//*[@id='all-show']/ul/li//div"):
            item = TaobaoItem()
            item['title'] = each.xpath("./p[@class='script-name']/a/text()").extract()
            item['pic'] = each.xpath(".//img/@src").extract_first()
            item['describtion'] = each.xpath("./p[@class='show-intro font-grey']/text()").extract()
            yield item
