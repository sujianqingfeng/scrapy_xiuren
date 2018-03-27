#!/usr/bin/env python
# encoding: utf-8

"""
@author: su jian
@contact: 121116111@qq.com
@file: run.py
@time: 2017/8/16 17:58
"""

from scrapy.cmdline import execute
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(['scrapy', 'crawl', 'xiuren_spider'])
# execute(['scrapy', 'crawl', 'meizi_spider'])


execute('scrapy crawl jcenter_spider'.split(' '))

# def func():
#     sys.path.append(os.path.dirname(os.path.abspath(__file__)))
#     execute(['scrapy', 'crawl', 'xiuren_spider'])
#
#
# if __name__ == '__main__':
#     func()

# import re
# print(re.findall(r'(\d+)', 'http://www.mzitu.com/57176')[0])
