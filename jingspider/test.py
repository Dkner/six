import requests
import re
from bs4 import BeautifulSoup

url = "https://www.kongjie.space/thread-10813866-1-1.html"
url_dict_pool = {}

response = requests.get(url)
print(response.text)
