import os
import json
from time import sleep
from random import randint

import redis

if __name__ == '__main__':
    redis_host = os.getenv('REDIS_HOST', 'queue')
    red = redis.Redis(host=redis_host, port=6379, db=0)
    print('Waiting messages...')
    while True:
        message = json.loads(red.blpop('sender')[1])
        # Simulating e-mail sending
        print('Sending message:', message['subject'])
        sleep(randint(15, 45))
        print('Message ', message['message'], ' sended!')
