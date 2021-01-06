// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
#include <math.h>
using namespace std;

class Polar
{
    float radius, angle;

public:
    void input()
    {
        cout << "Enter the Radius and Angle : ";
        cin >> radius >> angle;
    }
    void output()
    {
        cout << "\nPolar Form\nradius: " << radius << "m\nangle: " << angle << "°\n";
    }
    float getRadius()
    {
        return radius;
    }
    float getAngle()
    {
        return angle;
    }
};

class Rectangular
{
    float x, y;

public:
    void operator=(Polar P)
    {
        x = P.getRadius() * cos((P.getAngle() * M_PI) / 180);
        y = P.getRadius() * sin((P.getAngle() * M_PI) / 180);
    }
    void output()
    {
        cout << "\nRecatangular form\nx: " << x << "\ny: " << y << endl;
    }
};

int main()
{
    Polar pol;
    pol.input();
    pol.output();
    Rectangular rec;
    rec = pol;
    rec.output();
    return 0;
}

/*
OUTPUT

Enter the Radius and Angle : 7
45

Polar Form
radius: 7m
angle: 45°

Recatangular form
x: 4.94975
y: 4.94975

*/
