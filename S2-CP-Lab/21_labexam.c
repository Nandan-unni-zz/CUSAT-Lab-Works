// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>

int is_symmetric(int a[][10], int row, int col);
int upper(int a[][10], int row, int col);
int lower(int a[][10], int row, int col);

int main()
{
    int a[10][10], row, col, i, j, choice;
    printf("\nEnter the rows and column of the Matrix : ");
    scanf("%d %d", &row, &col);
    printf("\nEnter the Elements of the Matrix: \n");
    for (i = 0; i < row; i++)
    {
        for (j = 0; j < col; j++)
            scanf("%4d", &a[i][j]);
        printf("\n");
    }
    printf("1. Check whether matrix is symmetric");
    printf("\n2. Display the upper and lower matrix");
    printf("\nEnter your choice : ");
    scanf("%d", &choice);
    switch(choice)
    {
        case 1:
            is_symmetric(a, row, col);
            break;
        case 2:
            upper(a, row, col);
            lower(a, row, col);
            break;
        default:
            printf("\nInvalid choice !");
            break;
    }
    return 0;
}

int is_symmetric(int a[][10], int row, int col)
{
    int transpose[10][10], i, j, result = 1;
    for (i = 0; i < row; ++i)
        for (j = 0; j < col; ++j) {
            transpose[j][i] = a[i][j];
        }
    for (i = 0; i < row; ++i)
        for (j = 0; j < col; ++j)
        {
            if(transpose[i][j] != a[i][j])
                result = 0;
        }
    if (result == 1)
        printf("The array is symmetric");
    else
        printf("The array is not symmetric");
}


int upper(int a[][10], int row, int col)
{
    int i, j;
    printf("\n\n The upper matrix is : ");
    for(i = 0; i< row; i++){
        printf("\n");
        for(j = 0; j < col; j++){
            if(i > j){
                printf("0");
                printf("\t");
            }
            else{
                printf("%d\t", a[i][j]);

            }
        }
    }
}


int lower(int a[][10], int row, int col)
{
    int i, j;
    printf("\n\n The lower matrix is : ");
    for(i = 0; i < row; i++){
        printf("\n");
        for(j = 0; j < col; j++){
            if(i >= j){
                printf("%d\t", a[i][j]);
            }
            else{
                printf("0");
                printf("\t");
            }
        }
    }
}
