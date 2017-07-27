# -*- coding: utf-8 -*-

__author__ = 'dong anqi'

import os.path
rootdir = 'E:\迅雷下载'                                # 指明被遍历的文件夹
i = 0
f = open('E:/quiet.txt', 'w')                     #打开文件，若不存在则新建该文件

for parent, dirnames, filenames in os.walk(rootdir):  #三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
    for filename in filenames:                        #输出文件信息
        print(os.path.join(parent, filename))       #显示路径
        f.write(os.path.join(parent,filename))      #写入文件
        f.write('\n')                               #换行
        i += 1

print(i,' file(s)')
f.close()
