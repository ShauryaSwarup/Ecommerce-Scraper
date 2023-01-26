# This is a sample Python script.
from ecommercescraper.spiders.amazonspider import AmazonSpiderSpider
from ecommercescraper.spiders.flipkartspider import FlipkartSpider
from JSONAssembler import JSONAssembling
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
from twisted.internet import task
from scrapy.utils.project import get_project_settings
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    crawler = CrawlerProcess()

    def crawl(props):
        return crawler.crawl(props)

    def jsonassemble():
        JSONAssembling.jsonassemblefunc()

    def stopreactor():
        return reactor.stop()

    reactor.callLater(2, crawl, AmazonSpiderSpider)
    reactor.callLater(30, jsonassemble, )
    reactor.callLater(40, crawl, FlipkartSpider)
    reactor.callLater(480, stopreactor,)

    reactor.run()


if __name__ == '__main__':
    main()
