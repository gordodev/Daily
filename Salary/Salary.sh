#/bin/bash

#Purpose: Calculate hourly, wekly, monthly and anual salary based on what data is input

<<//// 

COMMENT: Strategy: you enter 50, that must mean hourly, assume, confirm, then calculate
If you enter 250,000, assume anual, confirm then calculate

NOTE:
9/19 21:26 Add loop at and where you run script again if person answers yes
////


FromAnual() {
echo "From anual"

}

FromHourly() {
echo "from hourly"
}


echo "Enter Salary: "
read Salary

if [ "$Salary" -gt "10000" ]; then
	echo "Is this anual?"
	FromAnual
elif [ "$Salary" -gt "7" -a "$Salary" -lt "200" ]; then
	echo "Is this hourly"
	FromHourly
else
	echo "nope, was that day rate?"
fi

#Loop?

#echo "Again?"
#read Again
read -p "Again? " -n 1 -r

if [[ $REPLY =~ ^[Yy]$ ]]; then	
	echo "Looping"
	sleep 0.4
	echo ""
	echo "GO!"
	sleep 0.2
	clear
	bash $0
else
	echo "no match for: $REPLY"
	exit
fi	
