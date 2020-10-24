// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    int range, i, j, flag;
    printf("Enter the range : ");
    scanf("%d", &range);
    if (range > 2)
        for (i = 2; i <= range; i++)
        {
            flag = 0;
            for (j = 2; j <= i/2; j++)
            {
                if (i % j == 0)
                    flag = 1;
            }
            if ( flag == 0)
                printf("%d, ", i);
        }
    else
        printf("only 2");
}

/*
OUTPUT


*/