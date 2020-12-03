// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
#include <math.h>

using namespace std;

class Shape
{
    protected:
        float perimeter, area;

    public:
        virtual void input() = 0;
        void output()
        {
            cout << "\nPerimeter = " << perimeter << " and Area = " << area;
        }
};

class Triangle : public Shape
{
    float side1, side2, side3;

    public:
        bool is_valid()
        {
            if (side1 <= 0 || side2 <= 0 || side3 <= 0)
                return false;
            if ((side1 + side2 < side3) || (side1 + side3 < side2) || (side2 + side3 < side1))
                {
                    return false;
                }
            return true;
        }
        void calculate()
        {
            if (!is_valid())
            {
                cout << "\nInvalid Sides !";
                perimeter = area = 0;
            }
            else
            {
                perimeter = side1 + side2 + side3;
                float s = (perimeter) / 2;
                area = sqrt(s * (s - side1) * (s - side2) * (s - side3));
            }
        }
        void input()
        {
            cout << "\n Enter the side lengths \n";
            cout << "\nLength of side 1: ";
            cin >> side1;
            cout << "Length of side 2: ";
            cin >> side2;
            cout << "Length of side 3: ";
            cin >> side3;
            calculate();
        }
};

class Rectangle : public Shape
{
    float length, breadth;

    public:
        bool is_valid()
        {
            if (length <= 0 || breadth <= 0)
                return false;
            return true;
        }
        void calculate()
        {
            if (!is_valid())
            {
                cout << "\nInvalid Sides !";
                area = perimeter = 0;
            }
            else
            {
                perimeter = 2 * (length + breadth);
                area = length * breadth;
            }
        }
        void input()
        {
            cout << "\nLength of Rectangle: ";
            cin >> length;
            cout << "Breadth of Rectangle: ";
            cin >> breadth;
            calculate();
        }
};

class Square : public Shape
{
    float side;

public:
    bool is_valid()
    {
        if (side <= 0)
            return false;
        return true;
    }
    void calculate()
    {
        if (!is_valid())
        {
            cout << "\nInvalid sides !";
            area = perimeter = 0;
        }
        else
        {
            perimeter = 4 * side;
            area = side * side;
        }
    }
    void input()
    {
        cout << "\nSide of Square : ";
        cin >> side;
        calculate();
    }
};

class Circle : public Shape
{
    float radius;

public:
    bool is_valid()
    {
        if (radius <= 0)
            return false;
        return true;
    }
    void calculate()
    {
        if (!is_valid())
        {
            cout << "\nInvalid radius !";
            area = perimeter = 0;
        }
        else
        {
            area = 3.14 * radius * radius;
            perimeter = 2 * 3.14 * radius;
        }
    }
    void input()
    {
        cout << "\nRadius of circle: ";
        cin >> radius;
        calculate();
    }
};


int main()
{
    int choice;
    bool online = true;
    Shape *shape;
    Triangle triangle;
    Rectangle rectangle;
    Square square;
    Circle circle;
    while (online)
    {
        cout << "Select your Shape : \n";
        cout << "\n1. Triangle \t2. Rectangle \n3. Square \t4. Circle \n5. Exit \n\n\t: ";
        cin >> choice;
        switch (choice)
        {
            case 1:
                shape = &triangle;
                shape -> input();
                shape -> output();
                break;
            case 2:
                shape = &rectangle;
                shape -> input();
                shape -> output();
                break;
            case 3:
                shape = &square;
                shape -> input();
                shape -> output();
                break;
            case 4:
                shape = &circle;
                shape -> input();
                shape -> output();
                break;
            case 5:
                cout << "\nExit\n";
                online = false;
                break;
            default:
                cout << "\nInvalid Choice! Try Again!";
                break;
        }
        cout << "\n_______________________________\n";
    }
    return 0;
}

/*
OUTPUT



*/
