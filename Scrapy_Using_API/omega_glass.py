import requests
import time

pconfig = {
    'proxyUser': 'qn4hibvl37fz',
    'proxyPass': 'x0pDfuYymtmwGLfI',
    'proxyHost': 'us.omegaproxy.com',
    'proxyPort': '6222'
}

# Set the number of requests to make before rotating the IP
requests_per_ip = 10

# Set the time interval to wait before rotating the IP (in seconds)
rotation_interval = 60

def rotate_ip(pconfig):
    # Use the Omega Proxy API to rotate the IP address
    api_url = "https://us.omegaproxy.com/api/v1/proxy/rotate"
    auth = (pconfig['proxyUser'], pconfig['proxyPass'])
    response = requests.post(api_url, auth=auth)
    if response.status_code == 200:
        new_proxy_host = response.json()['proxy_host']
        new_proxy_port = response.json()['proxy_port']
        pconfig['proxyHost'] = new_proxy_host
        pconfig['proxyPort'] = new_proxy_port
        proxies = {
            "http": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], pconfig['proxyHost'], pconfig['proxyPort']),
            "https": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], pconfig['proxyHost'], pconfig['proxyPort'])
        }
        return proxies
    else:
        print("Error rotating IP address:", response.text)
        return None

proxies = {
    "http": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], pconfig['proxyHost'], pconfig['proxyPort']),
    "https": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], pconfig['proxyHost'], pconfig['proxyPort'])
}

request_count = 0
last_rotation = time.time()

while True:
    url = "https://www.glassdoor.co.in/Job/mumbai-data-engineer-jobs-SRCH_IL.0,6_IC2851180_KO7,20.htm?locId=2851180&locT=C&sc.keyword=Data%20Engineer"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    result = requests.get(url=url, headers=headers, proxies=proxies)
    print(result.text)

    request_count += 1

    # Rotate the IP address after the specified number of requests
    if request_count >= requests_per_ip:
        request_count = 0
        last_rotation = time.time()
        new_proxies = rotate_ip(pconfig)
        if new_proxies is not None:
            proxies = new_proxies

    # Rotate the IP address after the specified time interval
    elif time.time() - last_rotation >= rotation_interval:
        last_rotation = time.time()
        new_proxies = rotate_ip(pconfig)
        if new_proxies is not None:
            proxies = new_proxies

    time.sleep(1)  # wait for 1 second before making the next request