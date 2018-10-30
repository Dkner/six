#coding=utf-8
import datetime
import os
import asyncio
import aiohttp
from aiohttp import web

routes = web.RouteTableDef()
local_storge_path = 'G:/spider_movie_storage'


@routes.get('/')
async def hello(request):
    return web.Response(text="Hello, world")


@routes.post('/get_ts')
async def get_ts(request):
    data = await request.post()
    title = data.get('title')
    url = data.get('url')
    print("[{}] get_ts:[{}-{}]".format(datetime.datetime.now(), title, url))
    if not os.path.exists('{}/{}'.format(local_storge_path, title)):
        os.mkdir('{}/{}'.format(local_storge_path, title))
    if os.path.exists('{}/{}/{}'.format(local_storge_path, title, url.split('/')[-1])):
        return web.Response(text="get_ts:[{}-{}] ok".format(title, url))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                with open('{}/{}/{}'.format(local_storge_path, title, url.split('/')[-1]), 'wb') as fd:
                    while True:
                        chunk = await resp.content.read(50)
                        if not chunk:
                            break
                        fd.write(chunk)
    return web.Response(text="[{}] get_ts:[{}-{}] ok".format(datetime.datetime.now(), title, url))

app = web.Application()
app.add_routes(routes)
web.run_app(app)