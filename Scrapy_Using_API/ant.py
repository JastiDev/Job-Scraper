import requests

# Set API key and URL
api_key = "8dc13b74f4ce4b798fb7185503b880db"
url = "https://in.indeed.com/jobs?q=&l=Ahmedabad%2C+Gujarat&vjk=46bc7135b8d55f27"

# Set headers
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Set payload
payload = {
    'url': url,
    'render_js': True,
    'wait_until': 'networkidle2',
    'timeout': 30
}

try:
    # Make API request to ScrapingAnt
    response = requests.post('https://api.scrapingant.com/scrape', headers=headers, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        html_content = response.json()['content']
        print(html_content)
    else:
        print(f"Error: {response.status_code} - {response.reason}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")