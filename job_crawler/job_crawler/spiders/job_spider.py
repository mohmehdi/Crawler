import scrapy
class JobSpider(scrapy.Spider):
    name = "jobsp"
    allowed_domains = ['www.freelancer.com']
    depth = 1
    urls = ""
    count = 0
    id = 0
    #custom_settings = {
    #    'DOWNLOAD_DELAY': 0.5,
    #}

    def start_requests(self):
        urls = self.urls.split(' ')
        self.depth = int(self.depth)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'depth': 0})
        self.count += len(urls)

    def parse(self, response):

        c_depth = response.meta.get('depth')

        print(f"{self.id} --> depth: {c_depth}")

        detail = ''.join(
            response.xpath('//*[@id="main"]/div/div/div/div[1]/section[1]/div/div[1]/div/p[not(@*)]/text()').getall())
        yield {
            'id': self.id,
            'job title': response.xpath('//h1[@class="PageProjectViewLogout-header-title"]/text()').get(),
            'location': response.xpath(
                '//span[@class="PageProjectViewLogout-detail-reputation-item-locationItem"]/text()').get().strip(),
            'skills': response.xpath('//a[@class="PageProjectViewLogout-detail-tags-link--highlight"]/text()').getall(),
            'details': detail,
            'time expire': response.xpath(
                '//span[@class="promotion-tag PageProjectViewLogout-promotionTag"]/text()').get().strip(),
            'budget': response.xpath('//p[@class="PageProjectViewLogout-header-byLine"]/text()').get()
        }
        self.id += 1

        if c_depth < self.depth:
            similar_jobs = response.xpath(
                '//*[@id="main"]/div/div/div/div[2]/aside/section[2]/div/div[2]/ul/li/a/@href').getall()
            self.count+=len(similar_jobs)
            print(f" found {len(similar_jobs)} links . total links: {self.count}")

            for href in similar_jobs:
                #print(href)
                yield response.follow(href, callback=self.parse, meta={'depth': (c_depth + 1)})


""" xpaths

     job title, location, skills, details, time expire, budget, similar jobs
     print(response.xpath('//h1[@class="PageProjectViewLogout-header-title"]/text()').get())

     job title
     response.xpath('//h1[@class="PageProjectViewLogout-header-title"]/text()').get()

     location
     response.xpath('//span[@class="PageProjectViewLogout-detail-reputation-item-locationItem"]/text()').get().strip()

     skills
     response.xpath('//a[@class="PageProjectViewLogout-detail-tags-link--highlight"]/text()').getall()

     details
     response.xpath('//*[@id="main"]/div/div/div/div[1]/section[1]/div/div[1]/div/p[not(@*)]/text()').getall()
     detail = (response.xpath('//*[@id="main"]/div/div/div/div[1]/section[1]/div/div[1]/div/p[not(@*)]/text()').getall())

     time expire
     response.xpath('//span[@class="promotion-tag PageProjectViewLogout-promotionTag"]/text()').get().strip()

     budget
     response.xpath('//p[@class="PageProjectViewLogout-header-byLine"]/text()').get()

     similar jobs
     response.xpath('//*[@id="main"]/div/div/div/div[2]/aside/section[2]/div/div[2]/ul/li/a/@href').getall()
    """

