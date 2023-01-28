import scrapy
from scrapy import Request
from ..items import mobileDetails
import json
import re

json_file_path = "/home/shaun/Desktop/Ecommerce-Scraper/amazon-assembled.json"
with open(json_file_path, 'r') as j:
    data = json.loads(j.read())


class FlipkartSpider(scrapy.Spider):
    name = 'flipkart'
    url = 'https://www.flipkart.com/search?q='
    # spaces are shown as %20 in the url
    count = len(data)
    i = 0

    custom_settings = {
        'DUPEFILTER_CLASS': 'scrapy.dupefilters.BaseDupeFilter',
    }

    object = data[i]
    search_query = object['model_name'] + " " + object['colour']
    search_query = search_query + " "
    for ele in object['storage_cap']:
        ele = str(ele).strip()
        search_query = search_query + ele + " "
    search_query = search_query[:-1]
    search_query.replace(" ", "%20")

    url = url + search_query

    def start_requests(self):
        yield Request(
            url=FlipkartSpider.url,
            callback=self.parse
        )

    def parse(self, response, **kwargs):

        details = mobileDetails()
        object = data[FlipkartSpider.i]
        titles = response.css('div._4rR01T::text').getall()
        flipkart_urls = response.css(
            'div._13oc-S>div>div._2kHMtA > a._1fQZEK::attr(href)').getall()
        flipkart_prices = response.css(
            'div._25b18c>div._30jeq3::text').getall()
        flipkart_star_ratings = response.css(
            'span > div._3LWZlK::text').getall()
        flipkart_no_ratings = response.css(
            'span._2_R_DZ>span>span::text').getall()

        details['flipkart_url'] = None
        details['flipkart_price'] = None
        details['flipkart_star_rating'] = None
        details['flipkart_no_rating'] = None

        j = 0

        for title in titles:
            try:
                if (re.search(object['model_name'], title, re.IGNORECASE)):
                    details['flipkart_url'] = "https://www.flipkart.com" + \
                        flipkart_urls[j]
                    details['flipkart_price'] = flipkart_prices[j].strip(
                        '\u20b9')
                    details['flipkart_star_rating'] = flipkart_star_ratings[j].strip()
                    details['flipkart_no_rating'] = flipkart_no_ratings[j].strip(
                        '\xa0')
                    yield (details)
                    break
                else:
                    if j <= len(flipkart_urls):
                        j += 1
                        continue
                    else:
                        break
            except IndexError:
                details['flipkart_url'] = None
                details['flipkart_price'] = None
                details['flipkart_star_rating'] = None
                details['flipkart_no_rating'] = None
                continue
            except:
                details['flipkart_url'] = None
                details['flipkart_price'] = None
                details['flipkart_star_rating'] = None
                details['flipkart_no_rating'] = None
                continue

        object['flipkart_url'] = details['flipkart_url']
        object['flipkart_price'] = details['flipkart_price']
        object['flipkart_star_rating'] = details['flipkart_star_rating']
        object['flipkart_no_rating'] = details['flipkart_no_rating']

        with open("final-flipkart-amazon-data.json", 'w') as jsonfile:
            json.dump(data, jsonfile)

        if (FlipkartSpider.i < FlipkartSpider.count):
            FlipkartSpider.i += 1
            object1 = data[FlipkartSpider.i]
            search_query = object1['model_name'] + " " + object1['colour']
            search_query = search_query + " "
            for ele in object1['storage_cap']:
                ele = str(ele).strip()
                search_query = search_query + ele + " "
            search_query = search_query[:-1]
            search_query.replace(" ", "%20")

            FlipkartSpider.url = 'https://www.flipkart.com/search?q=' + search_query

            yield Request(
                url=FlipkartSpider.url,
                callback=self.parse
            )
        else:
            pass
