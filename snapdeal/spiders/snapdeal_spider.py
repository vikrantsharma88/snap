from scrapy.spider import BaseSpider
from snapdeal.items import DealspiderItem
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.pipeline.images import ImagesPipeline


class SG_snapDeal_Spider(BaseSpider):
    name = 'SgsnapDeal'
    allowed_domains = ['snapdeal.com']
    start_urls = [
        'http://www.snapdeal.com',
        ]

    def parse(self, response):
        item = DealspiderItem()

        hxs = HtmlXPathSelector(response)
        description = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/a/div/div/text()').extract()  
        price = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/a/div/div/div/span/text()').extract()
        url = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/a/@href').extract()
        image_urls = hxs.select('/html/body/div/div/div/div/div/div/div/div/div/a/div/div/img/@src').extract()

        item['description'] = description
        item['price'] = price
        item['url'] = url
        item['image_urls'] = image_urls
        #works fine!!
        return item

SPIDER = SG_snapDeal_Spider()
