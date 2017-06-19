import scrapy
class HupuSpider(scrapy.spiders.Spider):
	name = 'market'
	start_urls = [
		"com.android.vending"
		]

	def parse(self, response):
		print(response.body)
