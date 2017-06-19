# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule,Spider
from scrapy.linkextractors import LinkExtractor
import json
from tutorial.items import LenovoItem


class YoukuSpider(CrawlSpider):
	name = 'youku'
	allowed_domains = ["youku.com"]
	start_urls = ["http://list.youku.com/show/id_z2072b3081d9811e6b2ad.html"]
	rules = [
		Rule(LinkExtractor(allow=(r'/show/id_.*')), callback="parse_item", follow=True),
		Rule(LinkExtractor(allow=(r'/show/.*')), follow=True)
		]
	
	def parse_item(self, response):
		#print(response.body)
		name = response.xpath("//li[@class='p-row p-title']/text()").extract()
		if len(name)>=1:
			title = response.xpath("//li[@class='p-row p-title']/a[@target='_blank']/text()").extract()
			playnums =  response.xpath("//div[@class='p-base']/ul/li")[9].extract()
			print(playnums)
	 
