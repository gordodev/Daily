#/bin/bash

#Purpose: Calculate hourly, wekly, monthly and anual salary based on what data is input

<<//// 

COMMENT: Strategy: you enter 50, that must mean hourly, assume, confirm, then calculate
If you enter 250,000, assume anual, confirm then calculate

NOTE:
9/19 21:26 Add loop at and where you run script again if person answers yes
9/21 15:56 Need to figure out a way to sanitize your inputs. Leave that for another project
////


FromAnual() {
echo "Seems to be annual..."
sleep 0.3
clear
#echo "That is \$$(expr $1 / 12) per month gross"
let "Monthly = $1 / 12"
echo "That is \$$Monthly per month gross"
sleep 0.4

}

FromHourly() {
echo "from hourly"
sleep 0.3
clear
let "Monthly = $Salary * 160"
echo "That is \$$Monthly per month gross."
#echo "That is \$$(expr $1 \* 40) per month"
}

clear
echo "Enter Salary: "
read Salary

if [ "$Salary" -gt "10000" ]; then
	echo "anual..."
	FromAnual $Salary
elif [ "$Salary" -gt "7" -a "$Salary" -lt "200" ]; then
	echo "hourly..."
	FromHourly
else
	echo "nope, was that day rate?"
fi

#Loop?

#echo "Again?"
#read Again
read -p "Again? " -n 1 -r

if [[ $REPLY =~ ^[Yy]$ ]]; then	
	clear
	echo "Looping"
	sleep 0.4
	echo ""
	echo "GO!"
	sleep 0.2
	clear
	bash $0
elif [[ $REPLY =~ ^[Nn] ]]; then
	clear
	echo "Until next time!"
	sleep 0.7
	clear
	pwd; date
else
	echo "no match for: \"$REPLY\""
	exit
fi	
