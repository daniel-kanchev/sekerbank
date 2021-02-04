import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from sekerbank.items import Article


class SekerSpider(scrapy.Spider):
    name = 'seker'
    allowed_domains = ['sekerbank.com.tr']
    start_urls = ['https://sekerbank.com.tr/hakkimizda/haberlervereklamfilmlerimiz/basinbultenleri',
                  'https://sekerbank.com.tr/hakkimizda/haberlervereklamfilmlerimiz/duyurular']

    def parse(self, response):
        links = response.xpath('//div[@id="sub-accordions"]//a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h1//text()').get().strip()

        date = response.xpath('//div[@class="col-md-2 sfnewsAuthorAndDate sfmetainfo"]//text()').get().strip()
        date = datetime.strptime(date, '%d.%m.%Y')
        date = date.strftime('%Y/%m/%d')
        content = response.xpath('//div[@class="sfnewsContent sfcontent"]//text()').getall()
        content = "\n".join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()