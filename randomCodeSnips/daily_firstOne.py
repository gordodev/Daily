#!/usr/bin/python3

#Program to find the first "1" in a list of randomly generated numbers

import random
import time

numbers=[]
numbersList=[]

def random_list():
    numbers=random.randrange(1000000000000, 1999999999999)
    print (numbers)
    global numbersList
    numbersList = [int(x) for x in str(numbers)]
    #return numbersList
    #print ("numbersList in random function: ",numbersList)

def first_one(num):              #Find first number
    #print (numbersList)   
    #print (num)
    found=0
    for x in num:
        if x == 1:
            found=1

while True:
    print ("This is your random number")
    random_list()
    print(numbersList)
    first_one(numbersList)
    time.sleep(0.5)
