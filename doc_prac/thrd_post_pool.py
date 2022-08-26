import requests
from concurrent.futures import ThreadPoolExecutor

def post_url(url, i):
    json_data = {"name" : f"user{i}"}
    return requests.post(url, json=json_data).json()

with ThreadPoolExecutor(max_workers=10) as pool:
    url_list = ["http://0.0.0.0:8000/greeting"]*100
    post_response_list = list(pool.map(post_url, url_list, [i for i in range(100)]))
    for response in post_response_list:
        print(response)
