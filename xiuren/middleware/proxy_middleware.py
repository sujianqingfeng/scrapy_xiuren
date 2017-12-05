# -*- coding: utf-8 -*-

import datetime
import os
# import random, requests, json


class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # ip = '45.76.238.192:{}'.format(random.randint(8110, 8145))


        # res = requests.get(url='http://127.0.0.1:6000/proxy/1.0.0/proxy', params={'site': 'ca'})
        # ip_json = json.loads(res.text)
        #
        # ip = '{}:{}'.format(ip_json['ip'], ip_json['port'])
        #
        # spider.logger.info('代理ip 地址--->{}'.format(ip))
        # request.meta['proxy'] = "http://{}".format(ip)
        pass


        # # 代理服务器
        # proxyServer = "http://proxy.abuyun.com:9020"
        #
        # # 代理隧道验证信息
        # proxyUser = "H4A7Z562648XD5GD"
        # proxyPass = "E67B2E17F8E52317"
        #
        # # for Python2
        # proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)
        #
        # request.meta["proxy"] = proxyServer
        #
        # request.headers["Proxy-Authorization"] = proxyAuth
