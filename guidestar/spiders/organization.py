import scrapy


class OrganizationSpider(scrapy.Spider):
    name = 'organization'
    allowed_domains = ['www.guidestar.org']
    start_urls = ['https://www.guidestar.org/nonprofit-directory/human-services/general-human-services/1.aspx']

    def parse(self, response):
        pass
