import scrapy

from xiaozong.items import XiaozongItem

class xiaozongSpider( scrapy.Spider ):
    name = "xiaozong"
    allowed_domains = ["appinn.com"]
    start_urls = ["http://www.appinn.com/"]

    def parse(self, response):
        for sel in response.xpath( "//div[@id='sidebar']/ul/li[2]/ul/li/a" ):
            item = XiaozongItem()
            item["title"] = sel.xpath( "@title" ).extract()
            item["link"] = sel.xpath( "@href" ).extract()
            yield item
            
