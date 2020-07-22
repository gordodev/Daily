#!/usr/bin/python3

#Find minimum


#Read numbers from user and insert into list

numbers=[]

while True:
    number=input('Enter number: \n')
    if number == '':    #If nothing entered, show minimum
        break
    numbers.insert(0,number)

# print minimum

print ('You entered the following: \n')
print (numbers)
print(min(numbers))
