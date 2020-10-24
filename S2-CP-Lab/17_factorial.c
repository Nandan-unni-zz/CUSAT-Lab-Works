// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>

int factorial(int n)
{
    if (n == 1)
        return n;
    else
        return n * factorial(n - 1);
}

void main()
{
    int n;
    printf("Enter the number : ");
    scanf("%d", &n);
    printf("%d! = %d\n", n, factorial(n));
}

/*
OUTPUT


*/