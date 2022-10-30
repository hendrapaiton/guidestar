from unicodedata import name
import scrapy


class GuidestarItem(scrapy.Item):
    name = scrapy.Field()
