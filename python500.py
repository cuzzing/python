#!/usr/bin/env python
# encoding=utf-8

__author__ = 'steady_animal'

import hashlib


def print_md5(a):
    md5 = hashlib.md5()
    md5.update(a.encode('utf-8'))
    return print(md5.hexdigest())


[print_md5(str(i)) for i in range(10)]
