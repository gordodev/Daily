#!/usr/bin/python3

#Program to find the first "1" in a list of randomly generated numbers

import random
import time

numbers=[]

def random_list():
    numbers=random.randrange(1000000000000, 1999999999999)
    print (numbers)
    numbersList = [int(x) for x in str(numbers)]
    print (numbers[0])


while True:
    print ("This is your random number")
    random_list()
    time.sleep(0.5)
