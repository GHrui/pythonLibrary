# -*- encoding:utf-8 -*-
# !/usr/bin/env python

import os
# 列出txt目录下所有的文件
files = os.listdir(".")
for filename in files:
    portion = os.path.splitext(filename)
    # 如果后缀是.kml
    if portion[1] == ".kml":
        # 重新组合文件名和后缀名
        newname = portion[0] + ".txt"
        os.rename(filename, newname)
