import requests
import json
import random
import time
import uuid
import boto3
import configparser

config = configparser.ConfigParser()
config.read('streaming.ini')

client = boto3.client('kinesis', region_name=config['streaming']['region'])
partition_key = str(uuid.uuid4())
counter = 0
while True:
    try:
        r = requests.get('https://randomuser.me/api/?exc=login')
        data = json.dumps(r.json(), ensure_ascii=False)
        counter += 1

        print(counter,
              client.put_record(
                  StreamName=config['streaming']['name'],
                  Data=data,
                  PartitionKey=partition_key)
              )
        time.sleep(random.uniform(0, 1))
    except json.decoder.JSONDecodeError as je:
        print(je)
        pass
