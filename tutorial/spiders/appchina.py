# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule,Spider
from scrapy.linkextractors import LinkExtractor
import json
from tutorial.items import LenovoItem


class AppChinaSpider(CrawlSpider):
	name = 'appchina'
	allowed_domains = ["appchina.com"]
	handle_httpstatus_list = [429]
	with open('/home/zhangyuxiang/Downloads/full_pkg.txt') as fi:
		start_urls = ['http://www.appchina.com/app/' + line.strip()  for line in fi.readlines()]
	#start_urls = ["http://www.appchina.com/app/com.ss.android.article.news"]
	rules = [Rule(LinkExtractor(allow=(r'/app/.*')), callback="parse", follow=True)]
	
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
		if response.status == 429:
			print('429'+'\t'+response.url)
			return
		url = response.url
		name = response.xpath("//h1[@class='app-name']/text()").extract()[0]
		score = response.xpath("//span[@class='app-statistic']/text()").extract()[0]
		#pkg = response.xpath("//a[@class='fl btn-8']/@data-pkgname").extract()[0]
		#downloads = response.xpath("//span[@class='fgrey5']/text()").extract()[0]
		classification = response.xpath("//div[@class='intro app-other-info-intro']/p[@class='art-content']/text()").extract()[4]
		download_url = response.xpath("//a[@class='download_app']/@onclick").extract()[0]
		print(name+'\t'+score+'\t' + '\t' + classification + '\t' + download_url + '\t' +url)
		#print(name+'\t'+score+'\t' + '\t'  + '\t' + classification  + '\t' +url)
		#print (download_url)

