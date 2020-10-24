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

        void swapReference(Swap& s)
        {
            int temp = s.a;
            s.a = s.b;
            s.b = temp;
        }

        void swapAddress(Swap* s)
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
        cout << "\n\n 1. Swap by value \t 2. Swap by Reference \n\n 3. Swap by Address \t 4. Exit \n\n\t Enter choice : ";
        cin >> choice;
        switch(choice)
        {
            case 1:
                cout << "\nSwap by Value \n";
                S.swapValue(S);
                S.output();
                break;
            case 2:
                cout << "\nSwap by Reference \n";
                S.swapReference(S);
                S.output();
                break;
            case 3:
                cout << "\nSwap by Address \n";
                S.swapAddress(&S);
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



*/
