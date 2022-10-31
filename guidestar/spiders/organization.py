import re
import scrapy


class OrganizationSpider(scrapy.Spider):
    name = 'organization'
    allowed_domains = ['www.guidestar.org']
    start_urls = [
        'https://www.guidestar.org/nonprofit-directory/human-services/general-human-services/'
    ]
    cur_pages = 1
    num_pages = 0

    def start_requests(self):
        url = self.start_urls[0] + str(self.cur_pages) + '.aspx'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        self.num_pages = response.xpath(
            '//p[@class="centered"]/a[contains(.,"End")]/@href'
        ).extract_first()
        self.num_pages = int(re.findall(r'\d+', self.num_pages)[0])
        if self.cur_pages < self.num_pages:
            self.cur_pages += 1
            next_pages = self.start_urls[0] + str(self.cur_pages) + '.aspx'
            yield response.follow(next_pages, self.parse)
