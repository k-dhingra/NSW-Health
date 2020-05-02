# -*- coding: utf-8 -*-
import scrapy, json
from covid_cases.items import CovidCasesItem


class PostcodeTestsSpider(scrapy.Spider):
    name = 'postcode_tests'

    def start_requests(self):
        url = 'https://nswdac-np-covid-19-postcode-heatmap.azurewebsites.net/datafiles/data_tests.json'

        yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):

        nsw_tests = json.loads(response.text)
        nsw_tests = nsw_tests['data']

        for i in nsw_tests:
            item = CovidCasesItem()

            item['Postcode'] = i['POA_NAME16']
            item['Tested'] = i['Number']
            item['Date'] = i['Date']

            yield item
