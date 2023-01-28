from urllib.parse import urlencode
import scrapy
from scrapy import Request
from ..items import mobileDetails
import re


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    allowed_domains = ['amazon.in']
    url = 'https://www.amazon.in/Today-Mobile-Offer/s?k=Today+Mobile+Offer'
    count = 1
    API = "e6f73cfd4908bd158531c8ac7978c3b5"

    def get_url(url):
        payload = {'api_key': AmazonSpiderSpider.API,
                   'url': url, 'country_code': 'in'}
        proxy_url = 'http://api.scraperapi.com/?' + urlencode(payload)
        return proxy_url

    def start_requests(self):
        yield Request(
            url=AmazonSpiderSpider.get_url(AmazonSpiderSpider.url),
            callback=self.parse
        )

    def parse(self, response, **kwargs):

        details = mobileDetails()

        url_phones = response.css(
            'div.s-product-image-container > div.aok-relative > span > a::attr(href)').getall()
        img_urls = response.css(
            'div.a-section>img.s-image::attr(src)').getall()
        titles = response.css('span.a-size-medium::text').getall()

        model_names = []
        brands = []
        colours = []
        storage_caps = []

        delimiter = "()|"
        for title in titles:
            words = list(filter(None, re.split(f'[{delimiter}]', title)))
            try:
                if words[0] == 'Renewed':
                    model_names.append(words[1])
                    brands.append(list(filter(None, (words[1].split(' '))))[0])
                    colours.append(
                        list(filter(None, (words[2].split(','))))[0])
                    storage_caps.append(
                        list(filter(None, (words[2].split(','))))[1:])

                else:
                    model_names.append(words[0])
                    brands.append(list(filter(None, (words[0].split(' '))))[0])
                    colours.append(
                        list(filter(None, (words[1].split(','))))[0])
                    storage_caps.append(
                        list(filter(None, (words[1].split(','))))[1:])

            except IndexError:
                continue

        details['url'] = url_phones
        details['title'] = titles
        details['brand'] = brands
        details['model_name'] = model_names
        details['price'] = response.css('span.a-price-whole::text').getall()
        details['star_rating'] = response.css('span.a-icon-alt::text').getall()
        details['no_rating'] = response.css(
            'span > a.a-link-normal s-underline-text s-underline-link-text s-link-style > span.a-size-base s-underline-text ::text').getall()
        details['colour'] = colours
        details['storage_cap'] = storage_caps
        details['img_url'] = img_urls

        yield details

        if AmazonSpiderSpider.count <= 20:
            AmazonSpiderSpider.count += 1
            AmazonSpiderSpider.url = 'https://www.amazon.in/Today-Mobile-Offer/s?k=Today+Mobile+Offer&page=' + str(
                AmazonSpiderSpider.count)
            yield Request(
                url=AmazonSpiderSpider.url,
                callback=self.parse
            )
        else:
            pass
