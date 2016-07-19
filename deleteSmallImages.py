#! /usr/bin/env python
# encoding=utf-8

import os
import stat


def get_dir_file(dirname):
    filelist = []
    for file in os.listdir(path=dirname):
        targetFile = os.path.join(dirname, file)
        filelist.append(targetFile)
    return filelist


def get_file_size(filename):
    return os.stat(filename)[stat.ST_SIZE]


if __name__ == '__main__':
    WORKDIR = 'E:\\downimg'
    filelist = get_dir_file(WORKDIR)
    for file in filelist:
        if (get_file_size(file) <= 1024 * 50 and os.path.exists(file)):
            os.remove(file)
            print("delete file %s" % (file))
        else:
            print("file not exists or file is well")
