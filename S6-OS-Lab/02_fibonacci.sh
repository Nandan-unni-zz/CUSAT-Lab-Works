#! /bin/bash

# A S Nandanunni
# Reg No: 20219023
# CS - A

echo "Enter the number of fibonacci terms to be displayed: "
read n

a=0
b=1
i=2

echo "The fibonacci series upto $n terms is: "
echo "$a"
echo "$b"

while [ $i -le $n ]
do
    c=$((a + b))
    echo $c
    a=$b
    b=$c
    i=$((i + 1))
done
