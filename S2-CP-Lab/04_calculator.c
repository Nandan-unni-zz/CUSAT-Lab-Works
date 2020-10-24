// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    float a, b;
    char op;
    printf("Enter the first number : ");
    scanf("%f", &a);
    printf("Enter the second number : ");
    scanf("%f", &b);
    printf("Enter the operator (+ , - , / , *) : ");
    scanf(" %c", &op);
    switch (op)
    {
        case '+':
            printf("\nThe sum of %f and %f is %f", a, b, a+b);
            break;
        
        case '-':
            printf("\nThe difference of %f and %f is %f", a, b, a-b);
            break;
        
        case '*':
            printf("\nThe product of %f and %f is %f", a, b, a*b);
            break;
        
        case '/':
            if ( b != 0)
                printf("\nThe quotient of %f and %f is %f", a, b, a/b);
            else
                printf("\nDivision by 0 is not possible");
            break;
        
        default:
            printf("\nInvalid Operator !");
            break;
    }
}

/*
OUTPUT


*/