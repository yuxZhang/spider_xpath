# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule,Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import json
from tutorial.items import LenovoItem


class HuaweiSpider(CrawlSpider):
	name = 'huawei_market'
	allowed_domains = ["huawei.com"]
	start_urls = ["http://appstore.huawei.com/app/C10085602"]
	rules = [
		Rule(LinkExtractor(allow=(r'/app/.*')), callback="parse_item", follow=True),
		Rule(LinkExtractor(allow=(r'/.*')), follow=True)
		]
	def start_requests(self):
		headers  ={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
		for url in self.start_urls:
			yield Request(url, headers=headers)
	def parse_item(self, response):
		url = response.url
		name = response.xpath("//span[@class='title']/text()").extract()[0]
		score = response.xpath("//ul[@class='app-info-ul nofloat']/li/p/span/@class").extract()[2]
		downloads = response.xpath("//ul[@class='app-info-ul nofloat']/li/p/span[@class='grey sub']/text()").extract()[0]
		downloads_url = response.xpath("//a[@class='mkapp-btn mab-install']/@dlurl").extract()[0]
		#print(name)
		print(name+'\t'+score+'\t'+downloads+'\t'+downloads_url+'\t'+url)
		#pkg = response.xpath("//a[@class='fl btn-8']/@data-pkgname").extract()[0]
		#downloads = response.xpath("//span[@class='fgrey5']/text()").extract()[0]
		#classification = response.xpath("//a[@class='fblue orange']/text()").extract()[-1]
		#download_url = response.xpath("//a[@class='icons btn-7 fl']/@href").extract()[0]
		#print(name+'\t'+score+'\t'+pkg + '\t' + downloads + '\t' + classification + '\t' + download_url + '\t' +url)
		

