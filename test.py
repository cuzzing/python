#!/usr/bin/env python
# encoding=utf-8

import requests
# import json
r = requests.get('http://movie.douban.com/top250/', headers={
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'})
print(r.url)
