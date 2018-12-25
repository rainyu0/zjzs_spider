# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZjzsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    area = scrapy.Field()
    level = scrapy.Field()
    spec_class = scrapy.Field()
    school_no = scrapy.Field()
    school_name = scrapy.Field()
    school_url = scrapy.Field()
    subject = scrapy.Field()
    specialities = scrapy.Field()
