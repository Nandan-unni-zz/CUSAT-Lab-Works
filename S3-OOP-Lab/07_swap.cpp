// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Swap
{
private:
    int a, b;

public:
    void swapValue(Swap s)
    {
        int temp = s.a;
        s.a = s.b;
        s.b = temp;
    }

    void swapReference(Swap &s)
    {
        int temp = s.a;
        s.a = s.b;
        s.b = temp;
    }

    void swapAddress(Swap *s)
    {

        int temp = s->a;
        s->a = s->b;
        s->b = temp;
    }

    void input()
    {
        cout << "\nEnter the values of a and b : ";
        cin >> a >> b;
    }
    void output()
    {
        cout << "\nThe values of the variables are : \n";
        cout << " a = " << a << "\n b = " << b << "\n";
    }
};

int main()
{
    int choice;
    bool online = true;
    Swap S;
    S.input();
    S.output();
    while (online)
    {
        cout << "\n_____________________________________________";
        cout << "\n\n 1. Swap by value \t 2. Swap by Reference \n\n 3. Swap by Address \t 4. Exit \n\n\t Enter choice : ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "\n\nSWAP BY VALUE \n";
            S.output();
            S.swapValue(S);
            cout << "\nAfter swap: \n";
            S.output();
            break;
        case 2:
            cout << "\n\nSWAP BY REFERENCE \n";
            S.output();
            S.swapReference(S);
            cout << "\nAfter swap: \n";
            S.output();
            break;
        case 3:
            cout << "\n\nSWAP BY ADDRESS \n";
            S.output();
            S.swapAddress(&S);
            cout << "\nAfter swap: \n";
            S.output();
            break;
        case 4:
            online = false;
        default:
            online = false;
            break;
        }
    }
    return 0;
}

/*
OUTPUT

Enter the values of a and b : 4
5

The values of the variables are : 
 a = 4
 b = 5

_____________________________________________

 1. Swap by value        2. Swap by Reference 

 3. Swap by Address      4. Exit 

         Enter choice : 1


SWAP BY VALUE 

The values of the variables are : 
 a = 4
 b = 5

After swap: 

The values of the variables are : 
 a = 4
 b = 5

_____________________________________________

 1. Swap by value        2. Swap by Reference 

 3. Swap by Address      4. Exit 

         Enter choice : 2


SWAP BY REFERENCE 

The values of the variables are : 
 a = 4
 b = 5

After swap: 

The values of the variables are : 
 a = 5
 b = 4

_____________________________________________

 1. Swap by value        2. Swap by Reference 

 3. Swap by Address      4. Exit 

         Enter choice : 3


SWAP BY ADDRESS 

The values of the variables are : 
 a = 5
 b = 4

After swap: 

The values of the variables are : 
 a = 4
 b = 5

_____________________________________________

 1. Swap by value        2. Swap by Reference 

 3. Swap by Address      4. Exit 

         Enter choice : 4

*/
