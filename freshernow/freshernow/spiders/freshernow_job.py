import scrapy

class JobSpider(scrapy.Spider):
    name = 'freshernow_job'
    allowed_domains = ['freshersnow.com']
    start_urls = ['https://www.freshersnow.com/government-jobs-india/']

    def parse(self, response):
        # Extract job data from the table
        for row in response.xpath('//tbody/tr'):
            yield {
                'Company': row.xpath('td[1]/strong/text()').get(),
                'Job Role': row.xpath('td[2]/text()').get(),
                'Qualification': row.xpath('td[3]/text()').get(),
                'Experience': row.xpath('td[4]/text()').get(),
                'Location': row.xpath('td[5]/text()').get(),
                'Apply Link': row.xpath('td[6]/a/@href').get(),
            }

# To run the spider, you can use the following command in your terminal:
# scrapy crawl freshernow_job -o output.json