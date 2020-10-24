// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    int no, a[20], i, j, temp;
    printf("\nEnter the number of elements in the array: ");
    scanf("%d", &no);
    printf("\nEnter the elements in the array: \n");
    for (i = 0; i < no; i++)
        scanf("%d", &a[i]);
    printf("\nThe Input array is : [ ");
    for (i = 0; i < no; i++)
        printf("%d, ", a[i]);
    printf("]\n");
    for (i = 0; i < no; i++)
        for (j = 0; j < no - i - 1; j++)
            if (a[j] > a[j + 1])
            {
                temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
    printf("\nThe Sorted Array is : [ ");
    for (i = 0; i < no; i++)
        printf("%d, ", a[i]);
    printf("]\n");
}

/*
OUTPUT


*/