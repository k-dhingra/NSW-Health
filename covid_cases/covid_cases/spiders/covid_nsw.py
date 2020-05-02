# -*- coding: utf-8 -*-
import scrapy, json
from covid_cases.items import CovidCasesItem


class CovidNswSpider(scrapy.Spider):
    name = 'covid_nsw'

    def start_requests(self):
        url = 'https://nswdac-np-covid-19-postcode-heatmap.azurewebsites.net/datafiles/data_Cases2.json'

        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        covid_nsw_data = json.loads(response.text)
        covid_nsw_data = covid_nsw_data['data']

        for i in covid_nsw_data:
            item = CovidCasesItem()

            item['Recovered'] = i['Recovered']
            item['Confirmed'] = i['Cases']
            item['Postcode'] = i['POA_NAME16']
            item['Deaths'] = i['Deaths']
            item['Date'] = i['Date']

            yield item
