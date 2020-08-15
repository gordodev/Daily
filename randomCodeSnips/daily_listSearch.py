#!/usr/bin/python3

#Search a list and find item


words = input("Enter a list of words: \n")
myList = words.split(' ')  #Split words by space


searchWord = input("What word you need?\n") #get search word

index = myList.index(searchWord) #Identify the index of word in question
print (index)


