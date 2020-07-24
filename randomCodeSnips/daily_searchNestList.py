#!/usr/bin/python3

#Application that will search for words in lists as well as in nexted lists
#In this case the list elements represent skills

import time

#Create empty lists

mainList=[]
subList=[]

while True:
    if len(subList)!=0:
        print('not')
        print('You want another?')
        time.sleep(2)
    if len(subList)==0:
        mainList.insert(0,subList)
        reply=input('Add to list?\n')
        if reply=="y" or reply=="Y":
            while True:
                #get list name & if nothing entered break
                skill=input("Enter UNIX synonym: \n")
                if skill=='':             #Exist loop if nothing entered
                    print('DONE!')
                    break
                subList.insert(0,skill)   #Populate list UNIX=[inserts,inserts]
        else:
            print('nope\n')
            break
    else:
        break
    #Split list items into seperate elements

    #insert into main list
print(subList)   
