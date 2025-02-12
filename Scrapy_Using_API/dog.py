
import requests
  
api_key = "66f6a500faa8d1032b6ff051"
url = "https://api.scrapingdog.com/linkedin"
  
params = {
      "api_key": api_key,
      "type": "profile",
      "linkId": "rbranson",
      "private": "false"
  }
  
response = requests.get(url, params=params)
  
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")