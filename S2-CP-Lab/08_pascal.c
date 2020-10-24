// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    int rows, i, j, k, no;
    printf("\n Enter the number of rows: ");
    scanf("%d", &rows);
    printf("\n");
    for (i = 0; i < rows; i++)
    {
        for (k = 1; k < rows - i; k++)
            printf("  ");
        for (j = 0; j <= i; j++)
        {
            if (j == 0)
                no = 1;
            else
                no = no * (i - j + 1) / j;
            printf(" %2d ", no);
        }
        printf("\n");
    }

}

/*
OUTPUT


*/