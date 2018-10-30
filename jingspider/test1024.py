import requests
import re
from bs4 import BeautifulSoup

url = "https://www.kongjie.space/forum-181-1.html"
url_dict_pool = {}

response = requests.get(url)
html_doc = response.text.encode(response.encoding).decode('utf-8')
soup = BeautifulSoup(html_doc)
links = soup.find_all("a", {"class": "s xst"}, href=True)
for link in links:
    if re.search(r'豪乳|巨乳|乳交|爆乳|爆奶|大奶|奶炮|大胸|丰乳|丰胸|G杯|E杯|F杯', str(link.string))\
            and not re.search(r'自慰|打飞机', str(link.string)):
        url_dict_pool[link.get('href')] = str(link.string)
print(url_dict_pool)