 # 

import scrapy

class JapaneseacSpider(scrapy.Spider):
    name = 'japaneseAC'
    allowed_domains = ['business.columbia.edu/']
    start_urls = ['https://business.columbia.edu/cjeb/research-publications/research-papers-archive/']

    def parse(self, response):
        contents = response.xpath('(//div[@class="field body field__item"])[1]/p[position()>3]')
        for content in contents:
            report_number = content.xpath('.//text()[1]').get()
            title = content.xpath('.//a/text()').get()
            link = content.xpath('.//@href').get()
            author = content.xpath('.//text()[2]').get()
            outlier = content.xpath('.//text()[3]').get()
            yield {
                'Report Number':report_number,
                'title':title,
                'link':link,
                'author':author,
                'outlier':outlier
            }
