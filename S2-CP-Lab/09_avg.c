// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    int a[20], no, i, sum = 0;
    float avg;
    printf("\n Enter the number of elements in the array: ");
    scanf("%d", &no);
    printf("\n Enter the elements: \n");
    for (i = 0; i < no; i++)
    {
        scanf("%d", &a[i]);
        sum += a[i];
    }
    avg = sum / no;
    printf("\nThe sum of the elements in the given array is %d", sum);
    printf("\nThe average of the elements in the given array is %f", avg);
}

/*
OUTPUT


*/