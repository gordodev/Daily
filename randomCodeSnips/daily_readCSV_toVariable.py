#!/usr/bin/python3

#Read columns to variable name

import csv

col1 = "Column1"
col2 = "Column2"
col3 = "Column3"

mydictionary={col1:[],col2:[],col3:[]}
csvFile = csv.reader(open("myfile.csv","r"))
for row in csvFile:
    mydictionary[col1].append(row[0])
    mydictionary[col2].append(row[1])
    mydictionary[col3].append(row[2])

print (mydictionary)
