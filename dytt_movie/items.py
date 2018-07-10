# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DyttMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cat = scrapy.Field()
    title = scrapy.Field()
    actor = scrapy.Field()
    hot_point = scrapy.Field()
    plot = scrapy.Field()
    magnetic_link = scrapy.Field()
    thunder_link = scrapy.Field()
    bt_link = scrapy.Field()

    pass
