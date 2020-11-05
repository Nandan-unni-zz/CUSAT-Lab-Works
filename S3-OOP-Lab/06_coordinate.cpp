// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
#include <math.h>
using namespace std;

void getCoordinate(int &x1, int &y1, int &x2, int &y2, int &x3, int &y3)
{
    cout << "Enter the 1st coordinates : ";
    cin >> x1 >> y1;
    cout << "Enter the 2nd coordinates : ";
    cin >> x2 >> y2;
    cout << "Enter the 3rd coordinates : ";
    cin >> x3 >> y3;
}

bool checkCoordinate(int &x1, int &y1, int &x2, int &y2, int &x3, int &y3)
{
    float check = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2;
    if (check == 0)
        return false;
    return true;
}

inline void getShortest(int x1, int y1, int x2, int y2, int x3, int y3)
{
    float l1, l2, l3, s;
    l1 = sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2));
    l2 = sqrt(pow((x2 - x3), 2) + pow((y2 - y3), 2));
    l3 = sqrt(pow((x3 - x1), 2) + pow((y3 - y1), 2));
    cout << "\nLenght btw 1st set : " << l1 << endl;
    cout << "Lenght btw 2nd set : " << l2 << endl;
    cout << "Lenght btw 3rd set : " << l3 << endl;
    cout << "\nThe shortest distance between the 3 coordintes is : ";
    cout << ((l1 > l2) ? ((l2 > l3) ? l3 : l2) : ((l1 > l3) ? l3 : l1)) << endl;
}

int main()
{
    int x1, x2, x3, y1, y2, y3;
    getCoordinate(x1, y1, x2, y2, x3, y3);
    if (checkCoordinate(x1, y1, x2, y2, x3, y3))
    {
        getShortest(x1, y1, x2, y2, x3, y3);
    }
    else
        cout << "\nInvalid coordinates";
    return 0;
}

/*
OUTPUT



*/
