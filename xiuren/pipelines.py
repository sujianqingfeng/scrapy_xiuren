# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class ImgSavePinpeline(ImagesPipeline):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding:': 'gzip, deflate',
        'Accept-Language': 'en_US,en;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': 'i.meizitu.net'
    }

    def get_media_requests(self, item, info):
        if info.spider.name == 'meizi_spider':
            yield scrapy.Request(item['image_url'], meta={'item': item}, headers=self.headers)
        else:
            yield scrapy.Request(item['image_url'], meta={'item': item})

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]

        if not image_paths:
            print('{}/{}------文件保存失败'.format(item['image_dir'], item['image_url']))
            raise DropItem("Item contains no images")
        else:
            print('{}/{}------文件保存成功'.format(item['image_dir'], item['image_url']))
        return item

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        base_name = os.path.basename(item['image_url'])
        index = item['image_dir'].find('（')
        if index == -1:
            index = item['image_dir'].find('(')
        if not index == -1:
            item['image_dir'] = item['image_dir'][:index]
        filename = u'{}/{}'.format(item['image_dir'], base_name)
        return filename
