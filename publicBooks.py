#!/usr/bin/env python
# encoding=utf-8
import requests
from bs4 import BeautifulSoup

def findBooks(url):
    res = requests.get(url)
    res.encoding = 'utf-8'
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    for books in soup.select('.border-wrap'):
        a = books.select('a')
        # print(a)
        if len(a) > 0:
            print(a[1].text, url + a[1]['href'])

counter = 0
while (counter < 241):
    findBooks('https://read.douban.com/provider/63698851/?cat=all&sort=top&start=' + str(counter))
    counter = counter + 30
