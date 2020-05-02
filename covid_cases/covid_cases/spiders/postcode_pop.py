# -*- coding: utf-8 -*-
import scrapy, json
from covid_cases.items import CovidCasesItem


class PostcodePopSpider(scrapy.Spider):
    name = 'postcode_pop'

    def start_requests(self):
        url = 'https://nswdac-np-covid-19-postcode-heatmap.azurewebsites.net/datafiles/population.json'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        covid_nsw_pop = json.loads(response.text)

        for i in covid_nsw_pop:

            item = CovidCasesItem()

            item['Postcode'] = i['POA_NAME16']
            item['Population'] = i['Tot_p_p']

            yield item
