// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>

int count(int *a, int n, int elm)
{
    int i, count = 0;
    for (i = 0; i < n; i++)
    {
        if (*a == elm)
            count++;
        a++;
    }
    return count;
}

void main()
{
    int a[20], n, i, cnt, elm;
    printf("Enter the no of elements : ");
    scanf("%d", &n);
    printf("Enter the elements :\n");
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("Enter the element to get the count : ");
    scanf("%d", &elm);
    printf("\nThere are %d occurances of element %d\n", count(&a[0], n, elm), elm);
}

/*
OUTPUT


*/