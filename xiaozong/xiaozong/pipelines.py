# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class XiaozongPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "v2exhot":
            item["link"] = "http://v2ex.com" + "".join(item["link"])
            return item
        else:
            return item
