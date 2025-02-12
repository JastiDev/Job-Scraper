
# import urllib.parse
# encoded_url = urllib.parse.quote("https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true',
#     params = { 
#          'block_ads': 'True',
#          'json_response': 'True',
#     }
# )

# print('Response HTTP Status Code: ', response.status_code)
# print('Response HTTP Response Body: ', response.content)




# import urllib.parse
# from bs4 import BeautifulSoup

# encoded_url = urllib.parse.quote("https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true',
#     params = { 
#          'block_ads': 'True',
#          'json_response': 'True',
#     }
# )

# print('Response HTTP Status Code: ', response.status_code)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'html.parser')

# # Find all job titles on the page
# job_titles = soup.find_all('h3', class_='t-16 t-bold')

# # Print the job titles
# for title in job_titles:
#     print(title.text.strip())

# # Find all job descriptions on the page
# job_descriptions = soup.find_all('p', class_='t-12 t-normal job-description')

# # Print the job descriptions
# for description in job_descriptions:
#     print(description.text.strip())

# # Find all company names on the page
# company_names = soup.find_all('p', class_='t-14 t-normal t-black')

# # Print the company names
# for company in company_names:
#     print(company.text.strip())

# # Find all locations on the page
# locations = soup.find_all('span', class_='job-result-card__location')

# # Print the locations
# for location in locations:
#     print(location.text.strip())





# import urllib.parse
# from bs4 import BeautifulSoup

# encoded_url = urllib.parse.quote("https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true',
#     params = { 
#          'block_ads': 'True',
#          'json_response': 'True',
#     }
# )

# print('Response HTTP Status Code: ', response.status_code)

# # Print the HTML content
# print(response.content)

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'lxml')

# # Find all job titles on the page
# job_titles = soup.find_all('h3', class_='t-16 t-bold')

# # Print the job titles
# for title in job_titles:
#     print(title.text.strip())




import urllib.parse
from bs4 import BeautifulSoup
import json

encoded_url = urllib.parse.quote("https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")

from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

response = client.get('https://www.linkedin.com/jobs/search/?currentJobId=3932150209&geoId=102713980&keywords=analyst&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true',
    params = { 
         'block_ads': 'True',
         'json_response': 'True',
    }
)

print('Response HTTP Status Code: ', response.status_code)

# Print the HTML content
print(response.content)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'lxml')

# Find all job titles on the page
job_titles = soup.find_all('h3', class_='t-16 t-bold')

# Print the job titles
for title in job_titles:
    print(title.text.strip())

# Find all job descriptions on the page
job_descriptions = soup.find_all('p', class_='t-12 t-normal job-description')

# Print the job descriptions
for description in job_descriptions:
    print(description.text.strip())

# Find all company names on the page
company_names = soup.find_all('p', class_='t-14 t-normal t-black')

# Print the company names
for company in company_names:
    print(company.text.strip())

# Find all locations on the page
locations = soup.find_all('span', class_='job-result-card__location')

# Print the locations
for location in locations:
    print(location.text.strip())

# Find all job links on the page
job_links = soup.find_all('a', class_='job-result-card__full-card-link')

# Print the job links
for link in job_links:
    print(link.get('href'))

# Find all job details on the page
job_details = soup.find_all('div', class_='job-result-card__contents job-result-card__contents--two-pane')

# Print the job details
for detail in job_details:
    print(detail.text.strip())

# Convert the response content to a JSON object
json_object = json.loads(response.content)

# Print the JSON object
print(json.dumps(json_object, indent=4))