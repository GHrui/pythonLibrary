# -*- encoding:utf-8 -*-
# !/usr/bin/env python
import os
path = "D:/CASSFILES/"
for filename in os.listdir(path):
    if os.path.splitext(filename)[1] == '.DAT':
        name = os.path.splitext(filename)[0]
        f = file(path + name + ".DAT", 'r')
        newf = open(path + "NEW" + name + ".DAT", 'w')
        lines = f.readlines()
        for line in lines[1:]:
            newline = line.split(',')[1].strip() + ',,' + line.split(',')[2] + ',' + line.split(',')[3] + ',' + line.split(',')[4]
            newf.write(newline + '\n')
        f.close()
        newf.close()