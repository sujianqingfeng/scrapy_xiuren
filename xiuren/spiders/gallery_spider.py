#!/usr/bin/env python
# encoding: utf-8

"""
@author: sujian
@contact: h121116111@gmail.com
@file: gallery_spider.py
@time: 2017/12/5 21:43
"""

import scrapy
from scrapy import Request
from xiuren.items import XiurenItem


class GallerySpider(scrapy.Spider):
    name = "gallery_spider"

    start_urls = ['http://www.55156.com/weimeiyijing/fengjingtupian']

    def parse(self, response):
        urls = response.xpath('//ul[@class="liL"]/li/a/@href').extract()

        self.logger.info('当前父图片urls----->{}'.format(urls))
        for url in urls:
            yield Request(url=url, callback=self.img_parse)
            # yield Request(url='http://www.55156.com/weimeiyijing/fengjingtupian/146515.html', callback=self.img_parse)

        next_page = response.css('.pages ul li ::attr(href)')[-2].extract()
        if next_page and not next_page == '#':
            self.logger.info('存在列表下一页------>{}'.format(next_page))
            yield Request(url=response.urljoin(next_page), callback=self.parse)

    def img_parse(self, respose):
        item = XiurenItem()
        img_url = respose.css('.articleBody p a img ::attr(src)').extract_first()
        img_dir = respose.css('.articleTitle h1 ::text').extract_first()

        item['image_url'] = img_url
        item['image_dir'] = img_dir

        next_page = respose.css('.pages ul li a ::attr(href)').extract()

        if next_page:
            next_page = next_page[-1]

        if next_page and not next_page == '#':
            self.logger.info('开始爬取图片下一页-------->{}'.format(next_page))
            yield Request(url=respose.urljoin(next_page), callback=self.img_parse)

        yield item
