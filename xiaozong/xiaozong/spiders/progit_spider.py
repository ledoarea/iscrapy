import scrapy
from xiaozong.items import ProgitItem


class ProgitSpider( scrapy.Spider ):
    name = "ProgitSpider"
    start_urls = ["http://git-scm.com/book/zh/v1"]
    
    def parse( self , response ):
        for sel in response.xpath("//li[@class='chapter']/h2 | //li[@class='chapter']/ol/li"):
            item = ProgitItem()
            item["title"] = sel.xpath("a/text()").extract()
            item["link"] = sel.xpath("a/@href").extract()
            item["number"] = sel.xpath("text()").extract()
            yield item
