import scrapy
from xiaozong.items import XiaozongItem

class v2exSpider( scrapy.Spider ):
    name = "v2exhot"
    allowed_domains = "v2ex.com"
    start_urls = ["http://v2ex.com/"]
    
    def parse( self , response ):
        for sel in response.xpath("//span[@class='item_hot_topic_title']"):
            item = XiaozongItem()
            item["title"] = sel.xpath("a/text()").extract()
            item["link"] = sel.xpath("a/@href").extract()
            yield item
