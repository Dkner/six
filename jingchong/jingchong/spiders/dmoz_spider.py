import scrapy
from jingchong.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://dmoztools.net/Computers/Programming/Languages/Python/Books/",
        # "http://dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] + '.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//div[@class="site-item "]'):
            item = DmozItem()
            item['title'] = sel.xpath('div[@class="title-and-desc"]/a/div[@class="site-title"]/text()').extract()[0]
            item['link'] = sel.xpath('div[@class="title-and-desc"]/a/@href').extract()[0]
            item['desc'] = sel.xpath('div[@class="title-and-desc"]/div[@class="site-descr "]/text()').extract()[0]
            print(item)
            yield item