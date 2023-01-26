# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcommercescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class mobileDetails(scrapy.Item):
    url=scrapy.Field()
    brand=scrapy.Field()
    title=scrapy.Field()
    model_name=scrapy.Field()
    price=scrapy.Field()
    star_rating = scrapy.Field()
    no_rating=scrapy.Field()
    colour=scrapy.Field()
    storage_cap =scrapy.Field()
    about_item =scrapy.Field()
    img_url = scrapy.Field()
    flipkart_url = scrapy.Field()
    flipkart_price = scrapy.Field()
    flipkart_star_rating = scrapy.Field()
    flipkart_no_rating = scrapy.Field()