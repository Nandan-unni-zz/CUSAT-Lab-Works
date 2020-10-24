// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
int main()
{
    int a[20][20], b[20][20], sum[20][20], product[20][20];
    int row_a, col_a, row_b, col_b, i, j, k;
    printf("\nEnter the rows and column of First Matrix : ");
    scanf("%d %d", &row_a, &col_a);
    printf("\nEnter the rows and column of Second Matrix : ");
    scanf("%d %d", &row_b, &col_b);
    if (col_a != row_b)
    {
        printf("\nMatrix Addition/Multiplication not possible.\n");
        return 0;
    }
    else
    {
        printf("\nEnter the Elements of Matrix A : \n");
        for (i = 0; i < row_a; i++)
        {
            for (j = 0; j < col_a; j++)
                scanf("%4d", &a[i][j]);
            printf("\n");
        }
        printf("\nEnter the Elements of Matrix B : \n");
        for (i = 0; i < row_b; i++)
        {
            for (j = 0; j < col_b; j++)
                scanf("%4d", &b[i][j]);
            printf("\n");
        }
        printf("\nMatrix A: \n");
        for (i = 0; i < row_a; i++)
        {
            for (j = 0; j < col_a; j++)
                printf("%4d", a[i][j]);
            printf("\n");
        }
        printf("\nMatrix B: \n");
        for (i = 0; i < row_b; i++)
        {
            for (j = 0; j < col_b; j++)
                printf("%4d", b[i][j]);
            printf("\n");
        }
        if (row_a != row_b || col_a != col_b)
            printf("\nMatrix addition not possible !");
        else
        {
            printf("\nSum of Matrix A and Matrix B :\n");
            for (i = 0; i < row_a; i++)
            {
                for (j = 0; j < col_a; j++)
                {
                    sum[i][j] = a[i][j] + b[i][j];
                    printf("%4d", sum[i][j]);
                }
                printf("\n");
            }
        }
        printf("\nProduct of Matrix A and Matrix B :\n");
        for (i = 0; i < row_a; i++)
        {
            for (j = 0; j < col_b; j++)
            {
                product[i][j] = 0;
                for (k = 0; k < col_a; k++)
                    product[i][j] += a[i][k] * b[k][j];
                printf("%4d", product[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}

/*
OUTPUT


*/