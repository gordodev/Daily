#!/bin/bash


#NOTE: Random script to catalog data and point out what you have most of as you add to inventory

touch inventory.dat

#Functions

InventoryIntake() {

echo "Enter Item"
read Item
clear
echo "$Item" >> inventory.dat #Add item to inventory
}

#Insert into file
#Design schema

#Count each item in file
#Figure out how to count each item

while true; do
	InventoryIntake

	#Sort list to get top item
	echo ""
	grep [a-Z] inventory.dat | sort -u >> ItemTypes.dat
	grep [a-Z] ItemTypes.dat | while read -r line ; do
	echo "$(grep -c $line inventory.dat),$line"; done >> UpdatedInventory.dat
	echo "Mostly $(grep [0-9] UpdatedInventory.dat | sort -r -t , -k 1 -g | head -1 | awk -F, '{print $2}')"

	#Clean up
	rm ItemTypes.dat
	rm UpdatedInventory.dat
	echo ""

done

#Display item

#Loop over




#while true; do echo "Enter Item"; read Item; clear; echo "$Item" >> inventory.dat ; echo ""; echo ""; grep [a-Z] inventory.dat | sort -u >> ItemTypes.dat;  grep [a-Z] ItemTypes.dat | while read -r line ; do  echo "$(grep -c $line inventory.dat),$line"; done >> UpdatedInventory.dat; echo "Mostly $(grep [0-9] UpdatedInventory.dat | sort -r -t , -k 1 -g | head -1 | awk -F, '{print $2}')"; rm ItemTypes.dat; rm UpdatedInventory.dat; echo ""; done#
