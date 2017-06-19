# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class DmozItem(scrapy.Item):
	title = scrapy.Field()
	link = scrapy.Field()
	desc = scrapy.Field()


class DoubanmoviveItem(scrapy.Item):
	name = Field()
	year = Field()
	score = Field()
	director = Field() 
	classification = Field()


class LenovoItem(scrapy.Item):
	name = Field()
	pkg = Field()
	url = Field()
	downloads = Field()
	score = Field()
