# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Trip01Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Hotel_name = scrapy.Field()
    Rank = scrapy.Field()
    Review = scrapy.Field()
    Address = scrapy.Field()
    Restaurant_nearby = scrapy.Field()
    pass
