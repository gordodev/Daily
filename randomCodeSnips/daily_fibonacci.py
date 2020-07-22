#!/usr/bin/python3

#Generate fibonacci

import time


#Init x/y values
x=1;y=1

#Functions:

def update_z(x,y):
    z=x+y
    return z

#Sequence counting loop
while True:
    #Add x+y to get first Z
    z=update_z(x,y)
    #print(z)
    
    #shift x & y values down to prepare for next calculation, sleep, then continue
    x=y;y=z
    #print (x,'+',y,'=',z)
    print (z)
    time.sleep(0.01)
