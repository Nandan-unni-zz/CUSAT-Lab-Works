// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
#include <math.h>
void main()
{
    int a, b, c;
    float d, e, f;
    printf("The quadratic eqn is a(x*x) + bx + c = 0");
    printf("\nEnter the coefficients :\n  a: ");
    scanf("%d", &a);
    printf("  b: ");
    scanf("%d", &b);
    printf("  c: ");
    scanf("%d", &c);
    printf("\nThe quadratic eqn is %d(x*x) + %dx + %d = 0", a, b, c);
    f = (b*b) - (4*a*c);
    if (f >= 0)
    {
        d = (b + sqrt(f)) / (2*a);
        e = (b - sqrt(f)) / (2*a);
        printf("\nThe roots of the quadratic eqn are %f and %f", d, e);
    }
    else
        printf("\nImaginary roots..!");
}

/*
OUTPUT


*/