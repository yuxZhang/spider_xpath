# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule,Spider
from scrapy.linkextractors import LinkExtractor
import json
from tutorial.items import LenovoItem


class TuniuSpider(CrawlSpider):
	name = 'lenovo_2'
	allowed_domains = ["lenovomm.com"]
	with open('/home/zhangyuxiang/Downloads/full_pkg.txt') as fi:
		start_urls = ['http://www.lenovomm.com/appdetail/' + line.strip() + '/0' for line in fi.readlines()]
	#start_urls = ["http://www.lenovomm.com/appdetail/com.tencent.news/0"]
	rules = [Rule(LinkExtractor(allow=(r'/appdetail/.*')), callback="parse", follow=True)]
	
####def parse_item(self, response):
####	#print(response.body)
####	url = response.url
####	name = response.xpath("//h1[@class='f18 fl']/text()").extract()[0]
####	score = response.xpath("//p[@class='starMBox cb fl']/@score").extract()[0]
####	pkg = response.xpath("//a[@class='fl btn-8']/@data-pkgname").extract()[0]
####	downloads = response.xpath("//span[@class='fgrey5']/text()").extract()[0]
####	classification = response.xpath("//a[@class='fblue orange']/text()").extract()[-1]
####	download_url = response.xpath("//a[@class='icons btn-7 fl']/@href").extract()[0]
####	print(name+'\t'+score+'\t'+pkg + '\t' + downloads + '\t' + classification + '\t' + download_url + '\t' +url)
		
	def parse(self, response):
		#print(response.body)
		url = response.url
		name = response.xpath("//h1[@class='f18 fl']/text()").extract()[0]
		score = response.xpath("//p[@class='starMBox cb fl']/@score").extract()[0]
		pkg = response.xpath("//a[@class='fl btn-8']/@data-pkgname").extract()[0]
		downloads = response.xpath("//span[@class='fgrey5']/text()").extract()[0]
		classification = response.xpath("//a[@class='fblue orange']/text()").extract()[-1]
		download_url = response.xpath("//a[@class='icons btn-7 fl']/@href").extract()[0]
		print(name+'\t'+score+'\t'+pkg + '\t' + downloads + '\t' + classification + '\t' + download_url + '\t' +url)
		

