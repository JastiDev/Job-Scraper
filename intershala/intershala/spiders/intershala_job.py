import scrapy

class InternshipSpider(scrapy.Spider):
    name = 'intershala_job'
    allowed_domains = ['internshala.com']
    start_urls = ['https://internshala.com/jobs/']

    def parse(self, response):
        # Extracting both existing internships and new internships
        internships = response.css('div.individual_internship, div.individual_internship_new')

        for internship in internships:
            yield {
                'job_title': internship.css('h3.job-internship-name a::text').get(),
                'company_name': internship.css('p.company-name::text').get().strip(),
                'location': internship.css('p.locations a::text').get(),
                'experience': internship.css('div.row-1-item:nth-child(2) span::text').get(),
                'salary': internship.css('div.row-1-item:nth-child(3) span.desktop::text').get().strip(),
                'posted_time': internship.css('div.status-success span::text').get(),
                'job_link': response.urljoin(internship.css('h3.job-internship-name a::attr(href)').get()),
                'actively_hiring': internship.css('div.actively-hiring-badge::text').get() is not None,  # True if actively hiring badge exists
                'job_type': internship.css('div.status-li span::text').get(),  # Extracts job type (e.g., Fresher Job)
                'early_applicant': internship.css('div.early_applicant_wrapper span::text').get() is not None,  # Checks if early applicant badge exists
            }

        # To follow pagination (if applicable)
        next_page = response.css('a.next_page::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)