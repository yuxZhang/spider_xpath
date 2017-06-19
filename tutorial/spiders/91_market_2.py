# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule,Spider
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
import json
from tutorial.items import LenovoItem


class JiuyiSpider(CrawlSpider):
	name = '91_market_2'
	allowed_domains = ["91.com"]
	with open('/home/zhangyuxiang/Downloads/full_pkg.txt') as fi:
		start_urls = ['http://apk.91.com/Soft/Android/' + line.strip() + '.html' for line in fi.readlines()]
	#start_urls = ["http://www.lenovomm.com/appdetail/com.tencent.news/0"]
	rules = [Rule(LinkExtractor(allow=(r'/Soft/.*')), callback="parse", follow=True)]
	
	
	def parse(self, response):
		url = response.url.strip()
		name = response.xpath("//h1[@class='ff f20 fb fl']/text()").extract()[0].strip()
		likes = response.xpath("//span[@class='ding spr']/text()").extract()[0].strip()
		dislikes = response.xpath("//span[@class='cai spr']/text()").extract()[0].strip()
		score = response.xpath("//span[@class='spr star']/a/@class").extract()[0].strip()
		downloads = response.xpath("//ul[@class='s_info']/li/text()").extract()[1].strip()
		downloads_url = response.xpath("//a[@class='s_btn s_btn3']/@data_url").extract()[0].strip()
		#print(downloads_url)
		print(url+'\t'+name+'\t'+likes+'\t'+dislikes+'\t'+score+'\t'+downloads+'\t'+downloads_url)
		#print(name+'\t'+score+'\t'+downloads+'\t'+downloads_url+'\t'+url)
		#pkg = response.xpath("//a[@class='fl btn-8']/@data-pkgname").extract()[0]
		#downloads = response.xpath("//span[@class='fgrey5']/text()").extract()[0]
		#classification = response.xpath("//a[@class='fblue orange']/text()").extract()[-1]
		#download_url = response.xpath("//a[@class='icons btn-7 fl']/@href").extract()[0]
		#print(name+'\t'+score+'\t'+pkg + '\t' + downloads + '\t' + classification + '\t' + download_url + '\t' +url)
		

