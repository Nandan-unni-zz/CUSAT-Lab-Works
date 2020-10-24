// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
#include <string.h>
void main()
{
    char names[20][10], temp[10];
    int n, i, j, k;
    printf("Enter the number of names : ");
    scanf("%d", &n);
    printf("Enter the %d names : \n", n);
    for (i = 0; i < n; i++)
        scanf("%s", names[i]);
    for (i = 0; i < n; i++)
    {
        k = 0;
        for (j = i; j < n; j++)
        {
            if (names[i][k] > names[j][k])
            {
                strcpy(temp, names[i]);
                strcpy(names[i], names[j]);
                strcpy(names[j], temp);
            }
        }
    }
    printf("\nThe names after sorting : \n");
    for (i = 0; i < n; i++)
        printf("%s\n", names[i]);
}

/*
OUTPUT


*/