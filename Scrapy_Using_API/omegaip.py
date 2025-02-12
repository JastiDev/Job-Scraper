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

proxies = {
    "http": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], pconfig['proxyHost'], pconfig['proxyPort']),
    "https": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], pconfig['proxyHost'], pconfig['proxyPort'])
}

request_count = 0
last_rotation = time.time()

while True:
    url = "https://www.glassdoor.co.in/Job/mumbai-data-engineer-jobs-SRCH_IL.0,6_IC2851180_KO7,20.htm?locId=2851180&locT=C&sc.keyword=Data%20Engineer"
    result = requests.get(url=url, proxies=proxies)
    print(result.text)

    request_count += 1

    # Rotate the IP address after the specified number of requests
    if request_count >= requests_per_ip:
        request_count = 0
        last_rotation = time.time()
        proxies = rotate_ip(pconfig)

    # Rotate the IP address after the specified time interval
    elif time.time() - last_rotation >= rotation_interval:
        last_rotation = time.time()
        proxies = rotate_ip(pconfig)

    time.sleep(1)  # wait for 1 second before making the next request

def rotate_ip(pconfig):
    # Use the Omega Proxy API to rotate the IP address
    api_url = "https://us.omegaproxy.com/api/v1/proxy/rotate"
    auth = (pconfig['proxyUser'], pconfig['proxyPass'])
    response = requests.post(api_url, auth=auth)
    if response.status_code == 200:
        new_proxy_host = response.json()['proxy_host']
        new_proxy_port = response.json()['proxy_port']
        proxies = {
            "http": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], new_proxy_host, new_proxy_port),
            "https": "http://{}:{}@{}:{}".format(pconfig['proxyUser'], pconfig['proxyPass'], new_proxy_host, new_proxy_port)
        }
        return proxies
    else:
        print("Error rotating IP address:", response.text)
        return None