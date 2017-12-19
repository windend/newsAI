# -*- coding: utf-8 -*-
import scrapy
from news.items import NewsItem
from scrapy.selector import Selector


class sinaNews(scrapy.Spider):
    name = 'sinaNews'
    default_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.anker.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }
    allowed_domains = ['anker.com']
    start_urls = ['https://www.anker.com/']  # 换网址

    # def parse(self, response):
    #     items = []
    #     for sel in response.xpath('//a'):
    #         item = NewsItem()
    #         # item['name'] = sel.xpath('text()').extract()
    #         item['image_urls'] = sel.xpath(
    #             'img/@src[contains(.,".jpg")]').extract()
    #         # item['decription'] = sel.xpath('text()').extract()
    #         yield item
    #         items.append(item)

    def parse(self, response):
        item = NewsItem()
        sel = Selector(response)
        item['name'] = sel.xpath('//a/text()').extract()
        item['image_urls'] = sel.xpath(
            '//a/img/@src[contains(.,".jpg")]').extract()
        yield item
