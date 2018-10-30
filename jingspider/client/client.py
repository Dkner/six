#coding=utf8
import os
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup
import re

base_url = "https://www.kongjie.space/forum-181-{}.html"

def get_movie_url_list(path):
    response = requests.get('http://{}'.format(domain, path))
    html_doc = response.text.encode(response.encoding).decode('utf-8')
    soup = BeautifulSoup(html_doc)
    src = soup.find(id='read_tpc').iframe.attrs.get('src')
    key_name = src.split('=')[-1]
    r = requests.get('https://m3u8.cdnpan.com/{}.m3u8'.format(key_name))
    return re.findall('https://.*out\d{3}\.ts', r.text)

async def get_ts(title, url):
    print('get_ts:{}'.format(url))
    payload = {
        'title': title,
        'url': url
    }
    async with aiohttp.ClientSession() as session:
        async with session.post('http://localhost:8080/get_ts', data=payload) as response:
            return await response.text()

async def download_page(page_no):
    url_dict_pool = {}
    response = requests.get(base_url.format(page_no))
    html_doc = response.text.encode(response.encoding).decode('utf-8')
    soup = BeautifulSoup(html_doc)
    links = soup.find_all("a", {"class": "s xst"}, href=True)
    for link in links:
        if re.search(r'豪乳|巨乳|乳交|爆乳|爆奶|大奶|奶炮|大胸|丰乳|丰胸|G杯|E杯|F杯', str(link.string)) \
                and not re.search(r'自慰|打飞机', str(link.string)):
            url_dict_pool[link.get('href')] = str(link.string)
    for path, title in url_dict_pool.items():
        print(path, title)
        url_list = get_movie_url_list(path)
        print(url_list)
        for url in url_list:
            await get_ts(title, url)

loop = asyncio.get_event_loop()
for page_no in range(1, 2):
    asyncio.ensure_future(download_page(page_no))
loop.run_forever()