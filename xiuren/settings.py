# -*- coding: utf-8 -*-


BOT_NAME = 'xiuren'

SPIDER_MODULES = ['xiuren.spiders']
NEWSPIDER_MODULE = 'xiuren.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 0

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# 请求头
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding:': 'gzip, deflate',
    'Accept-Language': 'en_US,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded'
}

DOWNLOADER_MIDDLEWARES = {
    'xiuren.middleware.proxy_middleware.ProxyMiddleware': 100,
    'xiuren.middleware.randomuseragent_middleware.RandomUserAgentMiddeleware': 101,
}

IMAGES_STORE = 'F:\\meizi'
ITEM_PIPELINES = {
    'xiuren.pipelines.ImgSavePinpeline': 300,
}
