import scrapy
from xiuren.items import XiurenItem
from scrapy import Request

'''
http://www.mzitu.com/japan/

'''

import re


class MeiziSpiders(scrapy.Spider):
    name = "meizi_spider"

    start_urls = ["http://www.mzitu.com/xinggan/", "http://www.mzitu.com/japan/", "http://www.mzitu.com/mm/",
                  "http://www.mzitu.com/taiwan/"]

    custom_settings = {

        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding:': 'gzip, deflate',
            'Accept-Language': 'en_US,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'www.mzitu.com',
            'Referer': 'http://www.mzitu.com'
        }

    }

    def parse(self, response):
        all_urls = response.xpath('//div[@class="postlist"]/ul/li/a/@href').extract()

        for url in all_urls:
            yield Request(response.urljoin(url), callback=self.parser_down)
            # yield Request(response.urljoin('http://www.mzitu.com/57176'),
            #               callback=self.parser_down)
            # pass
        self.logger.info('当前页urls--{}'.format(all_urls))

        next_page = response.css('a[class*=next] ::attr(href)').extract_first()

        if next_page:
            yield Request(response.urljoin(next_page), callback=self.parse)
            self.logger.info('当前页抓取完毕--开始下一页--{}'.format(next_page))
            pass

    def parser_down(self, response):

        item = XiurenItem()

        next_page = response.xpath('//div[@class="pagenavi"]/a/@href').extract()[-1].replace('#', '')
        img_link = response.xpath('//div[@class="main-image"]/p/a/img/@src').extract_first()
        img_dir = response.xpath('//h2[@class="main-title"]/text()').extract_first()

        item['image_dir'] = img_dir
        item['image_url'] = img_link
        self.logger.info('图片页面开始下载--{}--{}'.format(img_dir, img_link))

        if next_page and re.findall(r'(\d+)', response.url)[0] == re.findall(r'(\d+)', next_page)[0]:
            yield Request(response.urljoin(next_page), callback=self.parser_down)

        yield item
