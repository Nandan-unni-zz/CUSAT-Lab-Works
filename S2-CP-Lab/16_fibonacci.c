// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>

int fibonacci(int limit)
{
    if ( limit <= 1)
        return limit;
    else
        return fibonacci(limit - 1) + fibonacci(limit - 2);
}

void main()
{
    int limit, i;
    printf("Enter the limit of the series : ");
    scanf("%d", &limit);
    for (i = 0; i <= limit; i++)
        printf("%d, ", fibonacci(i));
}

/*
OUTPUT


*/