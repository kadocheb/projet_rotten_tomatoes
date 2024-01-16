# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class FilmItem(scrapy.Item):
    title = scrapy.Field()
    date = scrapy.Field()
    audience_score = scrapy.Field()
    critics_score = scrapy.Field()
    genre = scrapy.Field()
