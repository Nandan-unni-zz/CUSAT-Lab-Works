// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
#include <string.h>

struct Student
{
    char name[20];
    int m1, m2, m3, tot;
    float perc;
}s[50];


void main()
{
    int n, i;
    printf("Enter the number of students : ");
    scanf("%d", &n);
    for (i = 0; i < n; i++)
    {
        printf("\nStudent %d : \nEnter Name : ", i + 1);
        scanf("%s", s[i].name);
        printf("Enter the marks in Subject 1 :");
        scanf("%d", &s[i].m1);
        printf("Enter the marks in Subject 2 :");
        scanf("%d", &s[i].m2);
        printf("Enter the marks in Subject 3 :");
        scanf("%d", &s[i].m3);
        s[i].tot = s[i].m1 + s[i].m2 + s[i].m3;
        s[i].perc = s[i].tot / 3;
    }
    for (i = 0; i < n; i++)
    {
        printf("\n");
        puts(s[i].name);
        printf("Subject 1: %d\nSubject 2: %d\nSubject 3: %d\n", s[i].m1, s[i].m2, s[i].m3);
        printf("Total marks: %d\nPercentage: %f\n", s[i].tot, s[i].perc);
    }
}

/*
OUTPUT


*/