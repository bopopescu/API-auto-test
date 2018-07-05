# coding=utf8

import json
import traceback
import requests

url = "https://api.douban.com/v2/book/17604305?fields=id,title,url"
response = requests.get(url)
print(response.status_code)
if 'text' in response.text:
    print(response.text)
else:
    print"not find"

