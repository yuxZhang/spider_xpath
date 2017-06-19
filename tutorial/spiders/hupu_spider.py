import scrapy
class HupuSpider(scrapy.spiders.Spider):
	name = 'hupu'
	allowed_domains = ["dmoz.org"]
	start_urls = [
		"https://bbs.hupu.com/cba/",
		"https://bbs.hupu.com/all-nba/"
		]

	def parse(self, response):
		for x in response.url.strip().split("/"):
			#print(x)
			pass
		for title in response.xpath("//span[@class='red']/text()").extract():
			print(title)			
