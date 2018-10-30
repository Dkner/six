import logging
import async_timeout

logger = logging.getLogger(__name__)


class Lcurl(object):

    @staticmethod
    async def get(session, url, params={}, headers={}, response_type='json', timeout=5):
        try:
            with async_timeout.timeout(timeout):
                async with session.get(url, params=params, headers=headers) as r:
                    if r.status != 200:
                        return False
                    else:
                        if response_type == 'binary':
                            response = await r.read()
                        elif response_type == 'text':
                            response = await r.text()
                        else:
                            response = await r.json(content_type=None)
                        return response
        except Exception as e:
            logging.error('Lcurl get error:[{}]'.format(e))
            return False

    @staticmethod
    async def post(session, url, data='', headers={}, response_type='json', timeout=5):
        try:
            with async_timeout.timeout(timeout):
                async with session.post(url, data=data, headers=headers) as r:
                    if r.status != 200:
                        return False
                    else:
                        if response_type == 'binary':
                            response = await r.read()
                        elif response_type == 'text':
                            response = await r.text()
                        else:
                            response = await r.json(content_type=None)
                        return response
        except Exception as e:
            logging.error(e)
            return False

    @staticmethod
    async def post_json(session, url, json='', headers={}, response_type='json', timeout=5):
        try:
            with async_timeout.timeout(timeout):
                async with session.post(url, json=json, headers=headers) as r:
                    if r.status != 200:
                        return False
                    else:
                        if response_type == 'binary':
                            response = await r.read()
                        elif response_type == 'text':
                            response = await r.text()
                        else:
                            response = await r.json(content_type=None)
                        return response
        except Exception as e:
            logging.error(e)
            return False