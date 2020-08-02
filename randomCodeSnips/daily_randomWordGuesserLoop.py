#!/usr/bin/python3

#Picks random word form list, then tries to guess the word using loop

import random

words=[]

def get_words():
    while True:
        word=input("Enter some words: \n")
        if word == "":
            break
        words.insert(0,word)

get_words()
print ("You are done!\n[words]")
print (random.choice(words))



