// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
#include <math.h>
using namespace std;

class Triangle
{
private:
    float s1, s2, s3;
    float area;

public:
    bool is_valid;
    void input()
    {
        cout << "Enter the sides : ";
        cin >> s1 >> s2 >> s3;
    }
    void verify()
    {
        if (((s1 + s2) > s3) && ((s2 + s3) > s1) && ((s3 + s1) > s2))
            is_valid = true;
        else
            is_valid = false;
    }
    void disp_sides()
    {
        cout << "\nSides are " << s1 << ", " << s2 << " and " << s3 << "\n";
    }
    void disp_area()
    {
        int s = (s1 + s2 + s3) / 2;
        area = sqrt(s * (s - s1) * (s - s2) * (s - s3));
        cout << "\nThe area of the triangle is " << area << "\n";
    }
} t;

int main()
{
    t.input();
    t.verify();
    if (t.is_valid)
    {
        cout << "\nValid sides";
        t.disp_sides();
        t.disp_area();
    }
    else
        cout << "\nInvalid Sides";
    return 0;
}

/*
OUTPUT

Enter the sides : 3 4 5

Valid sides
Sides are 3, 4 and 5
The area of the triangle is 6


Enter the sides : 1 2 3

Invalid Sides

*/