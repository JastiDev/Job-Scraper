import requests
import urllib.parse
from bs4 import BeautifulSoup

def send_request(url):
    api_key = 'D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO'
    encoded_url = urllib.parse.quote(url, safe=':/')

    response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': api_key,
            'url': encoded_url  # Pass the url as a query parameter
        }
    )

    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the job data
    jobs = []
    for job in soup.find_all('div', {'class': 'job-result-card'}):
        title = job.find('h3', {'class': 'job-title'}).text.strip()
        company = job.find('h4', {'class': 'company'}).text.strip()
        location = job.find('span', {'class': 'location'}).text.strip()
        description = job.find('p', {'class': 'description'}).text.strip()
        job_data = f"Title: {title}, Company: {company}, Location: {location}, Description: {description}"
        print(job_data)
        jobs.append([title, company, location, description])
        print(job_data)

# Example usage:
url_to_scrape = 'https://www.linkedin.com/jobs/search/?currentJobId=4031817904&keywords=data%20scientist&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true'
send_request(url_to_scrape)
