# -*- encoding:utf-8 -*-
# !/usr/bin/env python

"""
This program converts each kml files to shp files.
"""

import arcpy
import os
import re

path = "../txt/"
files = os.listdir(path)
dir_name = os.path.dirname(os.path.dirname(os.path.abspath(files[0])))
prj = dir_name + "\\prj\\WGS 1984.prj"
pat = re.compile(r'<coordinates>')
for filename in files:
    portion = os.path.splitext(filename)
    basename = portion[0]
    openfile = open(dir_name + '\\txt\\' + filename, 'r')
    line = openfile.readline()
    while line:
        flag = pat.findall(line)
        if flag:
            coordinate_list = openfile.readline().strip()
            break
        line = openfile.readline()
    xyz_list = coordinate_list.split(' ')
    point_array = arcpy.Array()
    for xyz in xyz_list:
        point_xyz = xyz.split(',')
        point = arcpy.Point(X=point_xyz[0], Y=point_xyz[1], Z=point_xyz[2])
        point_array.add(point)
    feature = arcpy.Polygon(point_array, prj)
    arcpy.CopyFeatures_management(feature, dir_name + '\\shp\\' + basename + '.shp')
    openfile.close()
