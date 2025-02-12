import requests
from scrapingbee import ScrapingBeeClient

# Initialize ScrapingBee client
client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# Send request to LinkedIn job search page with extraction rules
response = client.get("https://www.linkedin.com/jobs/search/?currentJobId=4019792634&distance=25&geoId=102713980&keywords=data%20scientist&origin=JOBS_HOME_KEYWORD_HISTORY&refresh=true", 
                      params={'extract_rules': """
                              {
                                "job_postings": {
                                  "selector": "li.result-card.job-result-card.result-card--with-hover-state", 
                                  "extract": {
                                    "title": "h3.result-card__title", 
                                    "company": "h4.result-card__subtitle", 
                                    "location": "span.result-card__meta--location", 
                                    "description": "p.result-card__snippet"
                                  }
                                }
                              }
                              """})

# Extract data from response content in JSON format
data = response.json()

# Extract and print job data
for job in data['job_postings']:
    print('**Job Title:**', job['title'])
    print('**Company:**', job['company'])
    print('**Location:**', job['location'])
    print('**Description:**', job['description'])
    print('---')