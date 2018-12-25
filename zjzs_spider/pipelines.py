# -*- coding: utf-8 -*-

import codecs
import json

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ZjzsSpiderPipeline(object):
    def __init__(self):
        self.file = codecs.open('data_cn.json', 'wb', encoding='utf-8')

    def process_item(self, item, spider):
        # Notice: change list to string
        # print item['school_url']
        if type(item['school_url']) == tuple:
            item['school_url'] = item['school_url'][0]
        if type(item['school_name']) == tuple:
            item['school_name'] = item['school_name'][0]
        if type(item['school_no']) == tuple:
            item['school_no'] = item['school_no'][0]
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))
        return item



