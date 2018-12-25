#!/usr/bin/python
# -*- coding: utf-8 -*-

import scrapy
import time
from pyquery import PyQuery as pq

from zjzs_spider.items import ZjzsSpiderItem


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
        'http://zt.zjzs.net/xk2020/area_0_0.html',
        'http://zt.zjzs.net/xk2020/area_0_1.html',
        'http://zt.zjzs.net/xk2020/area_0_2.html',
        'http://zt.zjzs.net/xk2020/area_0_3.html',
        'http://zt.zjzs.net/xk2020/area_0_4.html',
        'http://zt.zjzs.net/xk2020/area_0_5.html',
        'http://zt.zjzs.net/xk2020/area_0_6.html',
        'http://zt.zjzs.net/xk2020/area_0_7.html',
        'http://zt.zjzs.net/xk2020/area_0_8.html',
        'http://zt.zjzs.net/xk2020/area_0_9.html',
        'http://zt.zjzs.net/xk2020/area_0_10.html',
        'http://zt.zjzs.net/xk2020/area_0_11.html',
        'http://zt.zjzs.net/xk2020/area_1_0.html',
        'http://zt.zjzs.net/xk2020/area_1_1.html',
        'http://zt.zjzs.net/xk2020/area_1_2.html',
        'http://zt.zjzs.net/xk2020/area_1_3.html',
        'http://zt.zjzs.net/xk2020/area_1_4.html',
        'http://zt.zjzs.net/xk2020/area_1_5.html',
        'http://zt.zjzs.net/xk2020/area_1_6.html',
        'http://zt.zjzs.net/xk2020/area_1_7.html',
        'http://zt.zjzs.net/xk2020/area_1_8.html',
        'http://zt.zjzs.net/xk2020/area_1_9.html',
        'http://zt.zjzs.net/xk2020/area_1_10.html',
        'http://zt.zjzs.net/xk2020/area_1_11.html',
        'http://zt.zjzs.net/xk2020/area_2_0.html',
        'http://zt.zjzs.net/xk2020/area_2_1.html',
        'http://zt.zjzs.net/xk2020/area_2_2.html',
        'http://zt.zjzs.net/xk2020/area_2_3.html',
        'http://zt.zjzs.net/xk2020/area_2_4.html',
        'http://zt.zjzs.net/xk2020/area_2_5.html',
        'http://zt.zjzs.net/xk2020/area_2_6.html',
        'http://zt.zjzs.net/xk2020/area_2_7.html'
    ]

    def parse(self, response):
        print 'parse: sleep 1 sec'
        time.sleep(1)
        all_area = response.xpath('//table/tr')
        for one_area in all_area:
            if len(one_area.css('td')) == 5 :
                if len(one_area.xpath('td')[3].xpath('a/@href').extract()) > 0 :
                    item = ZjzsSpiderItem()
                    item['area'] = one_area.xpath('td')[0].extract()[4:-5]
                    item['school_no'] = one_area.xpath('td')[1].extract()[4:-5],
                    item['school_name'] = one_area.xpath('td')[2].extract()[4:-5],
                    item['school_url'] = one_area.xpath('td')[3].xpath('a/@href').extract_first(),
                    inner_url = one_area.xpath('td')[4].xpath('a/@href').extract_first()
                    next_page = response.urljoin(inner_url)
                    request = scrapy.Request(next_page, callback=self.parse_speciality)
                    request.meta['item'] = item
                    yield request


    def parse_speciality(self, response):
        print 'parse_speciality: sleep 1 sec'
        time.sleep(0.3)
        item = response.meta['item']
        all_specs = response.xpath('//table/tr')
        for one_spec in all_specs:
            if len(one_spec.xpath('td')) == 4:
                level = pq(one_spec.xpath('td').extract()[0])('td').text()
                spec_class = pq(one_spec.xpath('td').extract()[1])('td').text()
                subject = pq(one_spec.xpath('td').extract()[2])('td').text()
                specialities = pq(one_spec.xpath('td').extract()[3])('td').text()
                item['level'] = level
                item['spec_class'] = spec_class.replace('\n', ',').replace('"', '').replace('\\', ' ')
                item['subject'] = subject.replace('\n', ',').replace('"', '').replace('\\', ' ')
                item['specialities'] = specialities.replace('\n', ',').replace('"', '').replace('\\', ' ')
                yield item


    # def start_requests(self):
    #     urls = [
    #             'http://zt.zjzs.net/xk2020/area_0_0.html'
    #         ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     all_area = response.xpath('//table/tr/td/a')
    #     print all_area
    #     outfile = open('out.txt', 'w')
    #     for one_area in all_area:
    #         item = one_area.extract().encode('utf-8')
    #         outfile.write(item)
    #         outfile.write('\n')
    #     outfile.close()

