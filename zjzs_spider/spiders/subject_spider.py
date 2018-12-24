#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy


# class SubjectSpider(scrapy.Spider):
#     name = "subject"
#
#     def start_requests(self):
#         urls = [
#             'http://quotes.toscrape.com/page/1/',
#             'http://quotes.toscrape.com/page/2/',
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)
#
#     def parse(self, response):
#         page = response.url.split("/")[-2]
#         filename = 'quotes-%s.html' % page
#         with open(filename, 'wb') as f:
#             f.write(response.body)
#         self.log('Saved file %s' % filename)

class SubjectSpider(scrapy.Spider):
    name = "subject"
    start_urls = [
        'http://zt.zjzs.net/xk2020/area_0_0.html'
    ]

    def start_requests(self):
        urls = [
                'http://zt.zjzs.net/xk2020/area_0_0.html'
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        all_area = response.xpath('//table/tr/td/a')
        print all_area
        outfile = open('out.txt', 'w')
        for one_area in all_area:
            item = one_area.extract().encode('utf-8')
            outfile.write(item)
            outfile.write('\n')
        outfile.close()

