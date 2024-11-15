import scrapy

class InternshipSpider(scrapy.Spider):
    name = 'intershala_job'
    allowed_domains = ['internshala.com']
    start_urls = ['https://internshala.com/jobs/work-from-home/']

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
                'actively_hiring': internship.css('div.actively-hiring-badge::text').get() is not None,
                'job_type': internship.css('div.status-li span::text').get(),
                'early_applicant': internship.css('div.early_applicant_wrapper span::text').get() is not None,
            }

        # Extract current page number and total pages
        current_page = response.css('#pageNumber::text').get()
        total_pages = response.css('#total_pages::text').get()

        # Debugging output
        print(f"Current Page: {current_page}, Total Pages: {total_pages}")  

        # Convert to integers if they are not None
        if current_page and total_pages:
            current_page = int(current_page)
            total_pages = int(total_pages)

            # Check if there is a next page
            if current_page < total_pages:
                next_page_number = current_page + 1
                next_page_url = f'https://internshala.com/jobs/work-from-home/page-{next_page_number}'
                print(f"Next page URL: {next_page_url}")  # Debugging output
                yield response.follow(next_page_url, self.parse)
        else:
            print("Could not extract current page or total pages.")  # Debugging output