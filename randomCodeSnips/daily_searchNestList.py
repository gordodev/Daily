#!/usr/bin/python3

#Application that will search for words in lists as well as in nexted lists
#In this case the list elements represent skills


#Create empty lists

mainList=[]
subList=[]

while True:
    #get list name & if nothing entered break
    skill=input("Enter UNIX synonym: \n")
    if skill=='':             #Exist loop if nothing entered
        print('DONE!')
        break
    subList.insert(0,skill)   #Populate list UNIX=[inserts,inserts]

    
    #Split list items into seperate elements

    #insert into main list
print(subList)   
