// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    int cu, cn;
    float rate;
    printf("Enter the Consumer no. : ");
    scanf("%d", &cn);
    printf("Enter the consumption units : ");
    scanf("%d", &cu);
    if ((cu >= 0) && (cu <=200))
        rate = 0.5 * cu;
    else if ((cu >= 201) && (cu <= 400))
        rate = 100 + (0.65 * (cu - 200));
    else if ((cu >= 401) && (cu <= 600))
        rate = 230 + (0.8 * (cu - 400));
    else
        rate = 390 + (cu - 600);
    printf("\nRate of charge is %f", rate);
}

/*
OUTPUT


*/