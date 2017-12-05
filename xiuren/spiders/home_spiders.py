import scrapy
from xiuren.items import XiurenItem
from scrapy import Request

'''
http:+-
网站主页的爬虫
'''


class XiuRenSpiders(scrapy.Spider):
    name = "xiuren_spider"

    start_urls = ["http://www.55156.com/gaoqingtaotu"]

    def parse(self, response):
        all_urls1 = response.xpath('//div[@class="labelbox_pic"]/ul/li/a/@href').extract()
        all_urls2 = response.xpath('//div[@class="columnt"]/span/a/@href').extract()
        all_urls3 = response.xpath('//div[@class="listBox"]/ul/li/a/@href').extract()
        all_urls = all_urls1 + all_urls2 + all_urls3
        all_urls = list(set(all_urls))

        for url in all_urls:
            yield Request(response.urljoin(url), callback=self.parser_down)
            # yield Request(response.urljoin('http://www.55156.com/a/pans/2014/1217/4295.html'),
            #               callback=self.parser_down)
            pass
        self.logger.info('当前页urls--{}'.format(all_urls))

        next_page = response.xpath('//div[@class="pages"]/ul/li/a/@href').extract()[-2].replace('#', '')

        if next_page:
            yield Request(response.urljoin(next_page), callback=self.parse)
            self.logger.info('当前页抓取完毕--开始下一页--{}'.format(next_page))

    def parser_down(self, response):

        item = XiurenItem()

        next_page = response.xpath('//div[@class="pages"]/ul/li/a/@href').extract()[-1].replace('#', '')
        img_link = response.xpath('//p[@align="center"]/a/img/@src').extract_first()
        img_dir = response.xpath('//div[@class="articleTitle"]/h1/text()').extract_first()

        item['image_dir'] = img_dir
        item['image_url'] = img_link
        self.logger.info('图片页面开始下载--{}--{}'.format(img_dir, img_link))

        if next_page:
            yield Request(response.urljoin(next_page), callback=self.parser_down)

        yield item
