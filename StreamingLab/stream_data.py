import requests
import json
import random
import time

while True:
    try:
        r = requests.get('https://randomuser.me/api/?exc=login')
        data = json.dumps(r.json(), ensure_ascii=False)
        print(data)
        time.sleep(random.uniform(0, 1))
    except json.decoder.JSONDecodeError as je:
        print(je)
        pass
