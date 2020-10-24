// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
#include <math.h>
using namespace std;

int power(int n, int p)
{
    return pow(n, p);
}

char power(char n, int p)
{
    return '?';
}

long power(long n, int p)
{
    return pow(n, p);
}

float power(float n, int p)
{
    return pow(n, p);
}
double power(double n, int p)
{
    return pow(n, p);
}

int main()
{
    int i = 2, p = 3;
    char c = 'b';
    long l = 2;
    float f = 2.0;
    double d = 2.0;
    printf("Int type overloaded func returned the value %d\n", power(i, p));
    printf("Char type overloaded func returned the value %c\n", power(c, p));
    printf("Long type overloaded func returned the value %ld\n", power(l, p));
    printf("Float type overloaded func returned the value %f\n", power(f, p));
    printf("Double type overloaded func returned the value %lf\n", power(d, p));
    return 0;
}

/*
OUTPUT



*/
