#!/usr/bin/python3

#Read all words in a file into a list

import re

job_description = []

with open("jobDescription.txt", "r") as f:
    for line in f:
        cleaned=re.sub(r'[^A-Za-z0-9 ]+', '', line)
        print (cleaned)
        #re.sub(r'\D', '', line)
        #re.sub(r'a', '', line)
        job_description.extend(cleaned.split())

print (job_description,"\n\n")

uniqueWords=[]
[uniqueWords.append(x) for x in job_description if x not in uniqueWords]

print (uniqueWords,"\n\n")

