#!/usr/bin/python3

#Read all words in a file into a list

job_description = []

with open("jobDescription.txt", "r") as f:
    for line in f:
        job_description.extend(line.split())

print (job_description)
