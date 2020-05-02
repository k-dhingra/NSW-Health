# -*- coding: utf-8 -*-
import scrapy, json
from covid_cases.items import CovidCasesItem


class PostcodeBoundariesSpider(scrapy.Spider):
    name = 'postcode_boundaries'

    def start_requests(self):
        url = 'https://nswdac-np-covid-19-postcode-heatmap.azurewebsites.net/datafiles/nswpostcodes_final.json'
        yield scrapy.Request(url=url, callback = self.parse)

    def parse(self, response):

        nsw_postcode_boundaries = json.loads(response.text)
        nsw_postcode_boundaries =  nsw_postcode_boundaries['features']

        for i in nsw_postcode_boundaries:
            item = CovidCasesItem()

            item['Postcode'] = i['properties']['POA_NAME16']
            item['Boundaries'] = i['geometry']['coordinates']

            yield item
