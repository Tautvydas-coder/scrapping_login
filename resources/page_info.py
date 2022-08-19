import requests
from resources.variables import *

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 '
                  'Safari/537.36'}


def check_web_status():
    page = requests.get(url=URL)
    print(page.status_code)
    if page.status_code == 403:
        print(page.status_code)
        page = requests.get(url=URL, headers=HEADERS)
        print(page)
    return page
