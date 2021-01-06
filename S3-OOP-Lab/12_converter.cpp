// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Distance
{
    int feet;
    float inch;

public:
    Distance()
    {
        feet = 0;
        inch = 0;
    }
    Distance(int meter)
    {
        inch = 39.37007874 * meter;
        feet = 0;
        if (inch > 12)
        {
            int old_feet = feet;
            feet += inch / 12;
            inch -= (feet - old_feet) * 12;
        }
    }
    void input()
    {
        cout << "\n\nEnter the distance in foot and inches : ";
        cin >> feet >> inch;
        if (inch > 12)
        {
            feet += inch / 12;
            inch -= feet * 12;
        }
    }
    void output()
    {
        cout << "The distance is " << feet << " feet, " << inch << " inches.";
    }
    operator float()
    {
        return (((feet * 12 + inch) * 2.54) / 100);
    }
};

int main()
{
    float m;
    Distance D;
    cout << "Enter the distance in meters : ";
    cin >> m;
    D = m;
    D.output();
    D.input();
    m = D;
    cout << "The distance is " << m << " meters.\n";
    return 0;
}

/*
OUTPUT

Enter the distance in meters : 10
The distance is 32 feet, 9.70078 inches.

Enter the distance in foot and inches : 5 4
The distance is 1.6256 meters.

*/
