import threading
import requests
import time

class post_greeting(threading.Thread):
    def __init__(self, name, num):
        # 부모클래스인 thread의 메소드와 속성 사용하기 위해
        # Thread.__init()
        super().__init__()
        self.name = name
        self.num  = num

    def run(self):
        print(threading.currentThread().getName(), " start!")

        json_data = {
            "name" : "user " + str(self.num)
        }
        print(json_data)
        response = requests.post('http://0.0.0.0:8000/greeting', json=json_data).json()
        print(response)

class get_greeting(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(threading.currentThread().getName(), " start!")
        response = requests.get('http://0.0.0.0:8000/greeting').json()
        # print(response)

print("post_greeting start")
for i in range(100):
    name = f"thread {i}"
    t = post_greeting(name, i)
    t.start()
print("post_greeting end")

print("get_greeting start")
for i in range(100):
    name = f"thread {i}"
    t = get_greeting(name)
    t.start()
print("get_greeting end")
