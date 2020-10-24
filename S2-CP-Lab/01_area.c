// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
int main()
{
    float lr, br, area_r, ht, bt, area_t;
    printf("Enter the length and breadth of Rectangle : \n");
    scanf("%f %f", &lr, &br);
    area_r = lr * br;
    printf("Area of the Rectangle is %f \n", area_r);
    printf("\nEnter the height and breadth of Triangle : \n");
    scanf("%f %f", &ht, &bt);
    area_t = 0.5 * ht * bt;
    printf("Area of the Triangle is %f", area_t);
    return 0;
}

/*
OUTPUT


*/