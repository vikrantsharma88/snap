from scrapy.item import Item

class OtherPipeline(object):
  def process_item(self, item, info):
    print "inside process"
    pass
