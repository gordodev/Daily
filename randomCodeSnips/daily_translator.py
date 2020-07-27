#!/usr/bin/python3

#Translate secret code

def to_carlcode(text):
    code= { 'c':'2','a':'0','r':'t','l':'1','y':'v','e':'3'}  #Dictionary
    carlcode=""

    for x in text:
        carlcode += code[x.lower()]

    return carlcode
test=input("enter word: \n")
print (to_carlcode(test))
