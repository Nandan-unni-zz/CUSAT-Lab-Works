// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
void main()
{
    char a[20], b[20], c[20], d[40], e[20];
    int la = 0, lb = 0, lc = 0, ld = 0, i, j, isSame = 1;
    printf("Enter string A : ");
    scanf("%s", a);
    for (i = 0; a[i] != '\0'; i++)
        la++;
    lb = la;
    lc = la;
    ld = lb + la;
    for (i = 0, j = lb - 1; i < la; i++, j--)
        b[j] = a[i];
    for (i = 0; i < la; i++)
    {
        c[i] = a[i];
        d[i] = a[i];
    }
    for (i = la, j = 0; i < ld; i++, j++)
        d[i] = b[j];
    printf("String A : %s\n", a);
    printf("Length of String A : %d\n", la);
    printf("String B (Reversed A) : %s\n", b);
    printf("String C (Copied String) : %s\n", c);
    printf("String D (Concatenated String) : %s\n", d);
    printf("Enter String E of %d length to compare with string A : ", la);
    scanf("%s", e);
    for (i = 0; i < la; i++)
        if (a[i] != e[i])
            isSame = 0;
    if (isSame)
        printf("String A and String E are same.");
    else
        printf("String A and String E are different.\n");
}

/*
OUTPUT


*/