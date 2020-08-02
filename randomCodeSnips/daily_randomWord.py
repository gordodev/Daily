#!/usr/bin/python3

#Picks random word form list

import random

words=[]

while True:
    word=input("Enter some words: \n")
    if word == "":
        break
    words.insert(0,word)

print ("You are done!\nwords")
print (random.choice(words))



