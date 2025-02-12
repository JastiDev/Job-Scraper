
# import urllib.parse
# encoded_url = urllib.parse.quote("https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d',
#     params = { 
#          'block_ads': 'True',
#          'json_response': 'True',
#     }
# )

# print('Response HTTP Status Code: ', response.status_code)
# print('Response HTTP Response Body: ', response.content)



# import urllib.parse
# from bs4 import BeautifulSoup

# encoded_url = urllib.parse.quote("https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d',
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

# encoded_url = urllib.parse.quote("https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d',
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


# import urllib.parse
# from bs4 import BeautifulSoup
# import json

# encoded_url = urllib.parse.quote("https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d',
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
# job_titles = soup.find_all('h2', class_='jobTitle-descriptor')

# # Print the job titles
# print("Job Titles:")
# for title in job_titles:
#     print(title.text.strip())

# # Find all company names on the page
# company_names = soup.find_all('span', class_='companyName')

# # Print the company names
# print("\nCompany Names:")
# for company in company_names:
#     print(company.text.strip())

# # Find all locations on the page
# locations = soup.find_all('div', class_='location')

# # Print the locations
# print("\nLocations:")
# for location in locations:
#     print(location.text.strip())

# # Find all job links on the page
# job_links = soup.find_all('a', class_='jcs-JobTitle')

# # Print the job links
# print("\nJob Links:")
# for link in job_links:
#     print(link.get('href'))

# # Find all job summaries on the page
# job_summaries = soup.find_all('div', class_='job-snippet')

# # Print the job summaries
# print("\nJob Summaries:")
# for summary in job_summaries:
#     print(summary.text.strip())

# # Convert the response content to a JSON object
# json_object = json.loads(response.content)

# # Print the JSON object
# print("\nJSON Object:")
# print(json.dumps(json_object, indent=4))



# import urllib.parse
# from bs4 import BeautifulSoup
# import json

# encoded_url = urllib.parse.quote("https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d")

# from scrapingbee import ScrapingBeeClient

# client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

# response = client.get('https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d',
#     params = { 
#          'block_ads': 'True',
#          'json_response': 'True',
#     }
# )

# if response.status_code == 500:
#     print("Error 500: Internal Server Error")
#     print("Please try again later")
# else:
#     print('Response HTTP Status Code: ', response.status_code)
#     # Rest of your code here

# # Parse the HTML content using BeautifulSoup
# soup = BeautifulSoup(response.content, 'lxml')

# # Find all job titles on the page
# job_titles = soup.find_all('h2', class_='jobTitle-descriptor')

# # Find all company names on the page
# company_names = soup.find_all('span', class_='companyName')

# # Find all locations on the page
# locations = soup.find_all('div', class_='location')

# # Find all job links on the page
# job_links = soup.find_all('a', class_='jcs-JobTitle')

# # Find all job summaries on the page
# job_summaries = soup.find_all('div', class_='job-snippet')

# # Create a list to store the job data
# job_data = []

# # Loop through the job titles and extract the data
# for i in range(len(job_titles)):
#     job = {
#         'title': job_titles[i].text.strip(),
#         'company': company_names[i].text.strip(),
#         'location': locations[i].text.strip(),
#         'link': job_links[i].get('href'),
#         'summary': job_summaries[i].text.strip()
#     }
#     job_data.append(job)

# # Print the job data in a formatted way
# print("Job Data:")
# for job in job_data:
#     print("Title: ", job['title'])
#     print("Company: ", job['company'])
#     print("Location: ", job['location'])
#     print("Link: ", job['link'])
#     print("Summary: ", job['summary'])
#     print("------------------------")


import urllib.parse
from bs4 import BeautifulSoup
import json

encoded_url = urllib.parse.quote("https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d")

from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

response = client.get('https://in.indeed.com/jobs?q=data+engineer&l=Ahmedabad%2C+Gujarat&from=searchOnDesktopSerp&vjk=d8574de41bb9943d',
    params = { 
         'block_ads': 'True',
         'json_response': 'True',
    }
)

if response.status_code == 200:
    print('Response HTTP Status Code: ', response.status_code)
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    # Find all job titles on the page
    job_titles = soup.find_all('h2', class_='jobTitle-descriptor')

    # Find all company names on the page
    company_names = soup.find_all('span', class_='companyName')

    # Find all locations on the page
    locations = soup.find_all('div', class_='location')

    # Find all job links on the page
    job_links = soup.find_all('a', class_='jcs-JobTitle')

    # Find all job summaries on the page
    job_summaries = soup.find_all('div', class_='job-snippet')

    # Create a list to store the job data
    job_data = []

    # Loop through the job titles and extract the data
    for i in range(len(job_titles)):
        job = {
            'title': job_titles[i].text.strip(),
            'company': company_names[i].text.strip(),
            'location': locations[i].text.strip(),
            'link': job_links[i].get('href'),
            'summary': job_summaries[i].text.strip()
        }
        job_data.append(job)

    # Print the job data in a formatted way
    print("Job Data:")
    for job in job_data:
        print("Title: ", job['title'])
        print("Company: ", job['company'])
        print("Location: ", job['location'])
        print("Link: ", job['link'])
        print("Summary: ", job['summary'])
        print("------------------------")
else:
    print("Error: ", response.status_code)