// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Distance
{
    int feet, inch;

public:
    void input()
    {
        cout << "Enter the feet and inch : ";
        cin >> feet >> inch;
        if (inch > 12)
        {
            feet += inch / 12;
            inch = inch % 12;
        }
    }
    void ouptut()
    {
        cout << feet << " feet " << inch << " inch " << endl;
    }

    Distance operator<(Distance d1)
    {
        Distance d2;
        if (d1.feet == feet)
        {
            if (d1.inch > inch)
            {
                d2.feet = d1.feet;
                d2.inch = d1.inch;
            }
            else
            {
                d2.feet = feet;
                d2.inch = inch;
            }
        }
        else if (d1.feet > feet)
        {
            d2.feet = d1.feet;
            d2.inch = d1.inch;
        }
        else if (d1.feet < feet)
        {
            d2.feet = feet;
            d2.inch = inch;
        }
        return d2;
    }

    friend Distance operator+(Distance, Distance);
};

Distance operator+(Distance d1, Distance d2)
{
    Distance d3;
    d3.inch = d1.inch + d2.inch;
    d3.feet = d1.feet + d2.feet;
    if (d3.inch > 12)
    {
        d3.feet += d3.inch / 12;
        d3.inch = d3.inch % 12;
    }
    return d3;
}

int main()
{
    Distance d1, d2, largest, sum;
    cout << "Enter the 1st distance\n";
    d1.input();
    cout << "\nEnter the 2nd distance\n";
    d2.input();
    cout << "\nDistance I : ";
    d1.ouptut();
    cout << "Distance II : ";
    d2.ouptut();
    sum = d1 + d2;
    largest = d1 < d2;
    cout << "\nThe largest of the two distances is ";
    largest.ouptut();
    cout << "The sum of the distances is ";
    sum.ouptut();
}

/*
OUTPUT

Enter the 1st distance
Enter the feet and inch : 5 4

Enter the 2nd distance
Enter the feet and inch : 6 10

Distance I : 5 feet 4 inch 
Distance II : 6 feet 10 inch 

The largest of the two distances is 6 feet 10 inch 
The sum of the distances is 12 feet 2 inch 

*/
