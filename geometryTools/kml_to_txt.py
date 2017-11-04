# -*- encoding:utf-8 -*-
# !/usr/bin/env python

import os
# 列出txt目录下所有的文件
path_list = ["\\Demo\\txt\\point", "\\Demo\\txt\\polygon", "\\Demo\\txt\\polyline"]
for path in path_list:
    files = os.listdir("." + path)
    dir_name = os.path.dirname(os.path.abspath(files[0]))
    for filename in files:
        portion = os.path.splitext(filename)
        # 如果后缀是.kml
        if portion[1] == ".kml":
            # 重新组合文件名和后缀名
            newname = portion[0] + ".txt"
            os.rename(dir_name + path + "\\" + filename, dir_name + path + "\\" + newname)
