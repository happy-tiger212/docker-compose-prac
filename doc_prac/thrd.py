import threading
import requests
import time

lock = threading.Lock()
class post_greeting(threading.Thread):
    def __init__(self, name, num):
        # 부모클래스인 thread의 메소드와 속성 사용하기 위해
        # Thread.__init()
        super().__init__()
        self.name = name
        self.num  = num

    def run(self):
        print(threading.currentThread().getName(), " post start!")
        # lock.acquire()
        json_data = {
            "name" : "user " + str(self.num)
        }
        response = requests.post('http://0.0.0.0:8000/greeting', json=json_data).json()
        # lock.release()
        print(response)
        

class get_greeting(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        # lock.acquire()
        print(threading.currentThread().getName(), " get start!")
        response = requests.get('http://0.0.0.0:8000/greeting').json()
        # lock.release()
        print(response)

print("greeting start")
for i in range(100):
    name = f"thread {i}"
    post_thread = post_greeting(name, i)
    get_thread = get_greeting(name)
# t.run()과의 차이점
    post_thread.start()
    get_thread.start()
    post_thread.join()
    get_thread.join()
print("greeting end")