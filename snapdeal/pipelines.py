from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy.http import Request

class MyImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        print "inside get_media_requests"
        for image_url in item['image_urls']:

            yield Request(image_url)

    def item_completed(self, results, item, info):

        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        print "inside item_completed"
        return item



    def process_item(self, item, spider):
        if spider.name == 'SgsnapDeal':
            print "inside process_item"
            # some code not relevant to the qn
            deal = DailyDeals(source_website_url=source_website_url,              source_website_logo=source_website_logo, description=description, price=price, url=url, image_urls=image_urls, city=city, currency=currency)
            deal.save()
