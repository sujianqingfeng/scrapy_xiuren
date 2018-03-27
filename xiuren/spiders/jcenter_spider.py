#!/usr/bin/env python
# encoding: utf-8

"""
@author: su jian
@contact: 121116111@qq.com
@file: jcenter_spider.py
@time: 2018/3/27 15:38
"""

import scrapy
from scrapy import Request


class JcenterSpider(scrapy.Spider):
    name = "jcenter_spider"

    start_urls = ["http://jcenter.bintray.com/"]

    def parse(self, response):
        hrefs = response.xpath('//pre/a/@href').extract()

        for href in hrefs:
            if '/' in href:
                yield Request(url=response.url + str(href).replace(':', ''), callback=self.parse)
            else:
                self.logger.info('连接----->{}'.format(response.url + href.replace(':', '')))
