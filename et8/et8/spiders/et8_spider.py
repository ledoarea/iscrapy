import scrapy
from et8.items import Et8Item

class Et8Spider( scrapy.contrib.spiders.CrawlSpider ):
    name = "et8_spider"
    start_urls = ["https://bbs.et8.net/bbs/forumdisplay.php?s=48aa6eae36c355403219ae8b22988c25&f=132"]
    rules = (
        Rule( SgmlLinkExtractor = () )
        )
 
