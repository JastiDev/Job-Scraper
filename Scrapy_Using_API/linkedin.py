
    # Install the Python ScrapingBee library:    
# pip install scrapingbee

from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='D04C6VXXXFHM99PPH0FHIY38XBGXBERCD1AXSSV427NZNG7SL1B7CLTRUFDDHJS9EEE3Y1GTZ48EBMLO')

response = client.get("https://www.linkedin.com/jobs/search?keywords=Data%20Specialist&location=Ahmedabad%2C%20Gujarat%2C%20India&geoId=104990346&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

print('Response HTTP Status Code: ', response.status_code)
print('Response HTTP Response Body: ', response.content)
