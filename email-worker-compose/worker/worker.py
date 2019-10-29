from time import sleep
from random import randint
import json

import redis

if __name__ == '__main__':
    red = redis.Redis(host='queue', port=6379, db=0)
    while True:
        message = json.loads(red.blpop('sender')[1])
        # Simulating e-mail sending
        print('Sending message:', message['subject'])
        sleep(randint(15, 45))
        print('Message ', message['message'], ' sended!')
