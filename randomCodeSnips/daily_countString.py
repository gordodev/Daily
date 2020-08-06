#!/usr/bin/python3

#Count the amount of times a string apears

import os

#get words from user
text=input("Enter text:\n")
os.system('clear')

word=input("Enter word to count:\n")
os.system('clear')

#Count the word and store in variable
count=text.count(word)

#Tell user how many found
print ('The word',word+', appears',count,'times.')

