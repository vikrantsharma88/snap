# Scrapy settings for snapdeal project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'snapdeal'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['snapdeal.spiders']
NEWSPIDER_MODULE = 'snapdeal.spiders'
DEFAULT_ITEM_CLASS = 'snapdeal.items.SnapdealItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)
ITEM_PIPELINES = ['scrapy.contrib.pipeline.images.ImagesPipeline', 'snapdeal.pipelines.MyImagesPipeline','snapdeal.otherpipelines.OtherPipeline']
IMAGES_STORE = '/home/kannu/snapdeal/dimages/full'

