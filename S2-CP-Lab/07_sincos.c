// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
#include <math.h>
void main()
{
    int no, i, j, k, factorial = 1, isPlus = 1;
    float x_deg, x_rad, term, sinx = 0, cosx = 0;
    printf("Enter the value of x (in degrees): ");
    scanf("%f", &x_deg);
    printf("\nEnter the number of terms: ");
    scanf("%d", &no);
    x_rad = x_deg * 3.14 / 180;
    printf("\n\nSine series = ");
    for (i = 1; i < 2 * no; i += 2)
    {
        factorial = 1;
        for (k = 1; k <= i; k++)
            factorial *= k;
        term = (pow(x_rad, i)) / factorial;
        if (isPlus)
        {
            printf("+");
            sinx += term;
            isPlus = 0;
        }
        else
        {
            printf("-");
            sinx -= term;
            isPlus = 1;
        }
        printf(" %f ", term);
    }
    printf("\n\nsin %f = %f \n", x_deg, sinx);

    isPlus = 1;
    printf("\n\nCosine series = ");
    for (i = 0; i < 2 * no; i += 2)
    {
        factorial = 1;
        for (k = 1; k <= i; k++)
            factorial *= k;
        term = (pow(x_rad, i)) / factorial;
        if (isPlus)
        {
            printf("+");
            cosx += term;
            isPlus = 0;
        }
        else
        {
            printf("-");
            cosx -= term;
            isPlus = 1;
        }
        printf(" %f ", term);
    }
    printf("\n\ncos %f = %f \n", x_deg, cosx);

}

/*
OUTPUT


*/