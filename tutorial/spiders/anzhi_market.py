# -*- coding: utf-8 -*-
from scrapy.selector import Selector
from scrapy.spiders import CrawlSpider,Rule,Spider
from scrapy.linkextractors import LinkExtractor
import json
from tutorial.items import LenovoItem


class TuniuSpider(CrawlSpider):
	name = 'anzhi_market'
	allowed_domains = ["anzhi.com"]
	start_urls = ["http://www.anzhi.com/soft_2802884.html"]
	rules = [
		Rule(LinkExtractor(allow=(r'/soft_\d*\.html')), callback="parse_item", follow=True),
		Rule(LinkExtractor(allow=(r'/.*')), follow=True)
	]	
	
	def parse_item(self, response):
		#print(response.body)
		url = response.url
		name = response.xpath("//div[@class='detail_line']/h3/text()").extract()[0]
	####score = response.xpath("//p[@class='starMBox cb fl']/@score").extract()[0]
	####pkg = response.xpath("//a[@class='fl btn-8']/@data-pkgname").extract()[0]
		#downloads = response.xpath("//ul[@class='detail_line_ul']").extract()
		downloads = response.xpath("//ul[@id='detail_line_ul']/li/span[@class='spaceleft']/text()").extract()[0]
	####classification = response.xpath("//a[@class='fblue orange']/text()").extract()[-1]
	####download_url = response.xpath("//a[@class='icons btn-7 fl']/@href").extract()[0]
	####print(name+'\t'+score+'\t'+pkg + '\t' + downloads + '\t' + classification + '\t' + download_url + '\t' +url)
		print (url+'\t'+name+'\t'+downloads)
		#print(name+'\t'+url+'\t'+downloads)

