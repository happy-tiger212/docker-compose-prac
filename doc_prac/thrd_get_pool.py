# 내 코드
import requests
from concurrent.futures import ThreadPoolExecutor
import threading

# def post_url(url, i):
#     json_data = {"name" : f"user{i}"}
    # return requests.post(url, json=json_data).json()
    
def get_url(url):
    return requests.get(url).json()

with ThreadPoolExecutor(max_workers=10) as pool:
    url_list = ["http://0.0.0.0:8000/greeting"]*100
    get_response_list = list(pool.map(get_url, url_list))
    for response in get_response_list:
        print(response)

# post get 섞어서
# url = "http://0.0.0.0:8000/greeting"
# executor = ThreadPoolExecutor(max_workers=10)
# for i in range(100):
    # post_request = executor.submit(post_url, url=url, i=i)
    # get_request = executor.submit(get_url, url=url)
    # print(post_request.result())
    # print(get_request.result())

# 돌아가는 코드 (post get 따로 나옴) 
# list1 = []
# with ThreadPoolExecutor(max_workers=10) as pool:
#     url_list = ["http://0.0.0.0:8000/greeting"]*10
#     post_response_list = list(pool.map(post_url, url_list, [i for i in range(100)]))
#     get_response_list = list(pool.map(get_url, url_list))
#     list1.extend(post_response_list)
#     list1.extend(get_response_list)
# for response in list1:
#     print(response)