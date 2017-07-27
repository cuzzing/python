#!/usr/bin/env python
# encoding=utf-8

import requests
from bs4 import BeautifulSoup

def copyContent(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')
    for content in soup.select('#mw-content-text'):
        print(content.text)

url = 'https://biblio.wiki/wiki/Nineteen_Eighty-Four/Part_I/Chapter_1'
copyContent(url)