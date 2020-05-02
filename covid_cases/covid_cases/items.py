# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CovidCasesItem(scrapy.Item):
    Recovered = scrapy.Field()
    Confirmed = scrapy.Field()
    Deaths = scrapy.Field()
    Postcode = scrapy.Field()
    Tested = scrapy.Field()
    Population = scrapy.Field()
    Suburb =  scrapy.Field()
    Date = scrapy.Field()
    Boundaries = scrapy.Field()
