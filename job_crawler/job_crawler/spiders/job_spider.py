import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')

        #job title, location, skills, details, time expire, budget, similar jobs

        #job title
        #response.xpath('//h1[@class="PageProjectViewLogout-header-title"]/text()').get()

        #location
        #response.xpath('//span[@class="PageProjectViewLogout-detail-reputation-item-locationItem"]/text()').get().strip()

        #skills
        #response.xpath('//a[@class="PageProjectViewLogout-detail-tags-link--highlight"]/text()').getall()

        #details
        #response.xpath('//p[not(@*)]/text()').getall()
        #detail = (response.xpath('//p[not(@*)]/text()').getall())
        #l = [i.strip('[]') for i in (response.xpath('//p[not(@*)]/text()').getall())]

        #time expire
        #response.xpath('//span[@class="promotion-tag PageProjectViewLogout-promotionTag"]/text()').get().strip()

        #budget
        #response.xpath('//p[@class="PageProjectViewLogout-header-byLine"]/text()').get()

        #similar jobs
        #//response.xpath('//*[@id="main"]/div/div/div/div[2]/aside/section[2]/div/div[2]/ul/li/a/@href').getall()
