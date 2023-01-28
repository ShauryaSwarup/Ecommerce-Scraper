# This is a sample Python script.
from ecommercescraper.spiders.amazonspider import AmazonSpiderSpider
from ecommercescraper.spiders.flipkartspider import FlipkartSpider
from JSONAssembler import JSONAssembling
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor
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

    def updatemongo():
        with open('/home/shaun/Desktop/Ecommerce-Scraper/server/mongoupdate.py') as infile:
            exec(infile.read())

    reactor.callLater(2, crawl, AmazonSpiderSpider)
    reactor.callLater(180, jsonassemble, )
    reactor.callLater(200, crawl, FlipkartSpider)
    reactor.callLater(850, updatemongo,)
    reactor.callLater(900, stopreactor,)
    reactor.run()


if __name__ == '__main__':
    main()
