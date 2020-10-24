// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
#include <math.h>

float mean(int data[15], int n)
{
    int sum = 0, i;
    float mn;
    for (i = 0; i < n; i++)
        sum += data[i];
    mn = sum / n;
    return mn;
}
float varience(int data[15], int n)
{
    int i;
    float sq_sum = 0, vr;
    for ( i = 0; i < n; i++)
        sq_sum += (data[i] * data[i]);
    vr = sq_sum / n;
    return vr;
}
float sdv(int data[15], int n)
{
    float vr = varience(data, n);
    float sd = sqrt(vr);
    return sd;
}

void main()
{
    int data[15], n, i;
    printf("Enter the no of elements : ");
    scanf("%d", &n);
    printf("\nEnter the dataset : \n");
    for (i = 0; i < n; i++)
        scanf("%d", &data[i]);
    printf("The of mean the data set is %f\n", mean(data, n));
    printf("The of varience the data set is %f\n", varience(data, n));
    printf("The of standard deviation the data set is %f\n", sdv(data, n));
}

/*
OUTPUT


*/