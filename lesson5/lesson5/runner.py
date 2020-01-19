from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from lesson5.lesson5 import settings
from lesson5.lesson5.spiders.spiders_hh import SpidersHhSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(SpidersHhSpider)
    process.start()