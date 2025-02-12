import scrapy

class FreshersnowSpider(scrapy.Spider):
    name = "freshersnow"
    start_urls = [
        'http://www.fresherworld.com/',
    ]

    def parse(self, response):
        # Extract all article links on the page
        article_links = response.css('article a::attr(href)').get()
        for link in article_links:
            yield response.follow(link, self.parse_article)

    def parse_article(self, response):
        # Extract article title and content
        title = response.css('h1.entry-title::text').get()
        content = response.css('div.entry-content::text').get()
        # Print the scraped data
        print("Title:", title)
        print("Content:", content)
        print("---")