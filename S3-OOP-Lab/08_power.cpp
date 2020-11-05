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
    return pow(n, p);
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
    cout << "Enter the power : ";
    cin >> p;
    cout << "\nEnter a int type value : ";
    cin >> i;
    cout << "Int type overloaded func returned the value " << power(i, p) << endl;
    cout << "\nEnter a char type value : ";
    cin >> c;
    cout << "Char type overloaded func returned the value " << power(c, p) << endl;
    cout << "\nEnter a long type value : ";
    cin >> l;
    cout << "Long type overloaded func returned the value " << power(l, p) << endl;
    cout << "\nEnter a float type value : ";
    cin >> f;
    cout << "Float type overloaded func returned the value " << power(f, p) << endl;
    cout << "\nEnter a double type value : ";
    cin >> d;
    cout << "Double type overloaded func returned the value " << power(d, p) << endl;
    return 0;
}

/*
OUTPUT



*/
