#!/bin/bash
i=0
while [ true ]
do
	myArray[$i]=$i
	i=$((i+1)) 
	echo $i
done
