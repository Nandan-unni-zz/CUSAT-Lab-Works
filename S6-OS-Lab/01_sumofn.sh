#! /bin/bash

# A S Nandanunni
# Reg No: 20219023
# CS - A

echo "Enter no of numbers: "
read n
sum=0
echo "Enter the $n numbers: "
for ((i = 0; i < $n; i++))
do 
  read a
  sum=$((a + sum))
done
echo "The sum is $sum"
