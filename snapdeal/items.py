from scrapy.item import Item, Field

class DealspiderItem(Item):
    description = Field()
    price = Field()
    url = Field()
    image_urls = Field()
    images = Field()
    image_paths = Field()
