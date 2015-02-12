from scrapy.contrib.spiders import CrawlSpider , Rule
from scrapy.selector import Selector
from xiaozong.items import XiaozongItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class XiaozongCrawlSpider( CrawlSpider ):
    name = "XiaozongCrawlSpider"
    start_urls = ["http://www.appinn.com/"]
    rules = (
        Rule(  
            SgmlLinkExtractor(
                allow = (), 
                restrict_xpaths = ("//*[@id='sidebar']/ul/li[2]")
            ),
            callback = "parse_item",
        ),
    )
    def parse_item(self, response):
        sel = Selector( response )
        item = XiaozongItem()
        item["title"] = sel.xpath("//h2/text()").extract() 
        item["link"] =  response.url
        item["desc"] = sel.xpath("//a[@class='comments-link']/text()").extract()
	yield item

