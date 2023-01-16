import scrapy


class ColumbiafdiSpider(scrapy.Spider):
    name = 'columbiaFDI'
    allowed_domains = ['ccsi.columbia.edu']
    start_urls = ['https://ccsi.columbia.edu/content/columbia-fdi-perspectives/']

    def parse(self, response):
        contents = response.xpath('(//div[@class="field field--name-field-cu-wysiwyg field--type-text-long field--label-hidden field--item"])[3]/p')
        for content in contents:
            report_number = content.xpath('.//strong/text()').get()
            title = content.xpath('.//a/text()').get()
            abstract = content.xpath('.//text()').get()
            link = content.xpath('.//@href').get()
            author = content.xpath('.//text()[2]').get()
            outlier = content.xpath('.//text()[3]').get()
            yield {
                'Report Number':report_number,
                'title':title,
                'abstract':abstract,
                'link':link,
                'author':author,
                'outlier':outlier
            }        
