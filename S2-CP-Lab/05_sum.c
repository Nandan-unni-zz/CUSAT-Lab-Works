// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    int num, copy, rem, sum = 0;
    printf("Enter a number : ");
    scanf("%d", &num);
    copy = num;
    while (copy > 0)
    {
        rem = copy % 10;
        sum += rem;
        copy /= 10;
    }
    printf("\nThe sum of the digits of the number %d is %d", num, sum);
}

/*
OUTPUT


*/