// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Complex
{
    int real, img;

public:
    Complex(int r = 0, int i = 0)
    {
        real = r;
        img = i;
    }
    friend ostream &operator<<(ostream &out, Complex &c);
    friend istream &operator>>(istream &in, Complex &c);
};

ostream &operator<<(ostream &out, Complex &c)
{
    out << c.real << " + " << c.img << "i " << endl;
    return out;
}

istream &operator>>(istream &in, Complex &c)
{
    cout << "Enter the real and imaginary parts : ";
    in >> c.real >> c.img;
    return in;
}

int main()
{
    Complex c;
    cin >> c;
    cout << "The complex object is ";
    cout << c;
    return 0;
}

/*
OUTPUT

Enter the real and imaginary parts : 3 4
The complex object is 3 + 4i 

*/
