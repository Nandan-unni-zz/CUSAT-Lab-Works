// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>

void linear(int a[20], int n, int el)
{
    int found = 0, i;
    for (i = 0; i < n; i++)
    {
        if (a[i] == el)
        {
            printf("%d found at position %d\n", el, i+1);
            found = 1;
        }
    }
    if (!found)
        printf("%d not found in array\n", el);
}
void binary(int a[20], int n, int el)
{
    int start, mid, end, i, j, found = 0;
    start = 0;
    mid = n / 2;
    end = n - 1;
    while (start < end)
    {
        if (el == a[mid])
        {
            printf("%d found at position %d\n", el, mid + 1);
            found = 1;
            break;
        }
        else if ( el < a[mid])
            end = mid - 1;
        else
            start = mid + 1;
    }
    if (!found)
        printf("%d not found in arrray\n", el);
}

void main()
{
    int a[20], n, i, ls, bs;
    printf("Enter the no of elements : ");
    scanf("%d", &n);
    printf("Enter the elements in increasing order : \n");
    for ( i = 0; i < n; i++)
        scanf("%d", &a[i]);
    printf("\nLinear Search\nEnter the number to search : ");
    scanf("%d", &ls);
    linear(a, n, ls);
    printf("\nBinary Search\nEnter the number to search : ");
    scanf("%d", &bs);
    binary(a, n, bs);
}

/*
OUTPUT


*/