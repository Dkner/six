import json
import logging
import asyncio
import aiohttp
from core.lcurl import Lcurl
import redis

logger = logging.getLogger(__name__)


class Worker(object):
    def __init__(self):
        self.q_k = 'test'
        self.loop = asyncio.new_event_loop()
        pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0, decode_responses=True)
        self.redis_client = redis.Redis(connection_pool=pool)
        self.buffer_size = 5
        self.buffer = []

    def run(self):
        while 1:
            flush_flag = False
            url = self.redis_client.blpop('test', timeout=5)
            print('pop:[{}]'.format(url))
            if url is None and self.buffer:
                flush_flag = True
            if url:
                self.buffer.append(url[1])
            if len(self.buffer)>=self.buffer_size:
                flush_flag = True
            if flush_flag:
                print('flush...')
                tasks, coroutines = [], []
                [coroutines.append(self.do_some_work(i)) for i in self.buffer]
                [tasks.append(self.loop.create_task(coroutine)) for coroutine in coroutines]
                [self.loop.run_until_complete(task) for task in tasks]
                self.buffer.clear()

    async def do_some_work(self, x):
        print('Waiting: ', x)
        await asyncio.sleep(int(x))
        print('Done:', x)


if __name__ == '__main__':
    worker = Worker()
    worker.run()