# -*- encoding:utf-8 -*-
# !/usr/bin/env python

"""
This program converts all points' kml files to one shp file.
"""

import arcpy
import re
import os

shp_name = 'city.shp'
in_path = ".\\Demo\\txt\\point"  # read this py file's path
files = os.listdir(in_path)
dir_name = os.path.dirname(os.path.abspath(files[0]))
prj = dir_name + "\\Demo\\prj\\WGS 1984.prj"  # Projection
flag = arcpy.Exists(dir_name + "\\Demo\\shp\\point\\" + shp_name)
if flag == 0:
    in_feature = arcpy.CreateFeatureclass_management(out_path=dir_name + "\\Demo\\shp\\point", out_name=shp_name, geometry_type="POINT", spatial_reference=prj)
    arcpy.AddField_management(in_feature, "CITY", "TEXT", field_length=50)
else:
    in_feature = dir_name + "\\Demo\\shp\\point\\" + shp_name
pat = re.compile(r'<coordinates>(.*?)</coordinates>')
pointGeometry_list = []
for filename in files:
    portion = os.path.splitext(filename)
    basename = portion[0]
    op_file = open(dir_name + "\\Demo\\txt\\point\\" + filename, 'r')
    line = op_file.readline()
    while line:
        coord = re.findall(pattern=pat, string=line)
        if coord:
            break
        else:
            line = op_file.readline()
    coord[0].strip()
    xyz = coord[0].split(',')
    point = arcpy.Point(X=xyz[0], Y=xyz[1], Z=xyz[2])
    pointGeometry = arcpy.PointGeometry(point)
    pointGeometry_list.append([pointGeometry, basename])
    op_file.close()
cursor = arcpy.InsertCursor(in_feature, ["CITY"])
for point_insert in pointGeometry_list:
    row = cursor.newRow()
    row.Shape = point_insert[0]
    row.CITY = point_insert[1]
    cursor.insertRow(row)
del row
del cursor
