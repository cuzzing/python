#!/usr/bin/env python
# encoding=utf-8

__author__ = 'steady_animal'

import requests
from bs4 import BeautifulSoup
import time

def recordAmount(id):                              # find amounts of songs listened to and print it
    url = 'http://music.163.com/user/home?id=' + id
    res = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'})
    res.encoding = 'utf-8'
    # print(res.text)
    soup = BeautifulSoup(res.text, 'html.parser')
    result = soup.select('h4')[0].text
    # print(result)
    print(onlyNumberInStr(result))

def onlyNumberInStr(mixedStr):              # extract numbers in str
    return ''.join(list(filter(str.isdigit, mixedStr)))

name = ['姜鸡',
        '人鱼',
        '挺爷',
        '滚滚',
        '一鸣',
        '撸枫',
        '老章',
        'she',
        'MoSheng',
        'myself',
        '机长',
        '某朱']
id = ['122804072',
      '249973578',
      '46366826',
      '386283936',
      '44768275',
      '320060179',
      '103419354',
      '321401740',
      '277733522',
      '29919246',
      '319832486',
      '360870567']

# recordAmount('122804072')

for index in range(len(id)):
    print(name[index], end=' ')
    recordAmount(id[index])

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))