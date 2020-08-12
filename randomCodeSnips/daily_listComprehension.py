#!/usr/bin/python3

#List comprehension

input_list = [1,2,3,4,4,5,6,7,7]
output_list=[]

for var in input_list:
    if var % 2 == 0:
        if var not in output_list:
            output_list.append(var)
print ("", output_list)


input_list=[1,2,3,4,4,5,6,7,7]
list_using_comp = [var for var in input_list if var % 2 == 0]

print ("We are here", list_using_comp)
