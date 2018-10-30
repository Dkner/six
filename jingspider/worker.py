import json
import logging
import asyncio
import aiohttp
from core.lcurl import Lcurl

logger = logging.getLogger(__name__)


class Worker(object):
    def __init__(self):
        self._loop = asyncio.new_event_loop()

    def run(self):
        try:
            logger.warning('worker run...')
            asyncio.ensure_future(coro_or_future=self.do_job(), loop=self._loop)
            self._loop.run_forever()
        except Exception as e:
            logger.error(e)
            asyncio.gather(*asyncio.Task.all_tasks()).cancel()
        finally:
            self._loop.close()

    async def do_job(self):
        while True:
            await asyncio.sleep(1)


if __name__ == '__main__':
    worker = Worker()
    worker.run()