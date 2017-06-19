# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule,Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import json
from tutorial.items import LenovoItem


class JiuyiSpider(CrawlSpider):
	name = '91_market'
	allowed_domains = ["91.com"]
	start_urls = ["http://apk.91.com/Soft/Android/com.taobao.trip-8100013.html"]
	rules = [Rule(LinkExtractor(allow=(r'/Soft/Android/.*')), callback="parse_item", follow=True)]
	
	def parse_item(self, response):
		url = response.url.strip()
		name = response.xpath("//h1[@class='ff f20 fb fl']/text()").extract()[0].strip()
		likes = response.xpath("//span[@class='ding spr']/text()").extract()[0]
		dislikes = response.xpath("//span[@class='cai spr']/text()").extract()[0]
		#score = response.xpath("//ul[@class='app-info-ul nofloat']/li/p/span/@class").extract()[2]
		#downloads = response.xpath("//ur[@class='s_info']/li/text()").extract()[0]
		#downloads_url = response.xpath("//a[@class='s_btn s_btn3']/@data_url").extract()[0]
		#print(url+'\t'+name)
		print(url+'\t'+name+'\t'+likes+'\t'+dislikes)
		#print(name+'\t'+score+'\t'+downloads+'\t'+downloads_url+'\t'+url)
		#pkg = response.xpath("//a[@class='fl btn-8']/@data-pkgname").extract()[0]
		#downloads = response.xpath("//span[@class='fgrey5']/text()").extract()[0]
		#classification = response.xpath("//a[@class='fblue orange']/text()").extract()[-1]
		#download_url = response.xpath("//a[@class='icons btn-7 fl']/@href").extract()[0]
		#print(name+'\t'+score+'\t'+pkg + '\t' + downloads + '\t' + classification + '\t' + download_url + '\t' +url)
		

