// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Employee
{
    protected:
        string name;
        long int emp_no;
        float pay_rate;

    public:
        Employee()
        {
            cout << "\nEnter the name of the Employee: ";
            cin >> name;
            cout << "Enter the Employee Number: ";
            cin >> emp_no;
            cout << "Enter the Pay Rate: ";
            cin >> pay_rate;
        }
        virtual void pay()
        {
            cout << "\nPay Rate: " << pay_rate;
        }
};

class Manager : public Employee
{
    bool issalaried;
    public:
        Manager()
        {
        PayMethodPortal:
            cout << "\nSelect Manager's Pay Method : ";
            cout << "\n1. Hourly Basis \n2. Salary Basis \n\n\t : ";
            int choice;
            cin >> choice;
            if (choice == 1)
                issalaried = false;
            else if (choice == 2)
                issalaried = true;
            else
            {
                cout << "\nInvalid Choice! Try Again!";
                goto PayMethodPortal;
            }
        }
        void pay()
        {
            if (issalaried)
            {
                cout << "\nPay Rate : " << pay_rate;
            }
            else
            {
                float hours_worked;
                cout << "\nEnter the no of hours worked: ";
                cin >> hours_worked;
                cout << "Amount Paid : " << hours_worked * pay_rate;
            }
        }
};

class Supervisor : public Employee
{
    string department;
    public:
        Supervisor()
        {
            cout << "\nEnter the department: ";
            cin >> department;
        }
        void pay()
        {
            cout << "\nPay rate : " << pay_rate;
        }
};


int main()
{
    int choice;
    bool online = true;
    char ch;
    Manager M;
    Supervisor S;
    while (online)
    {
        cout << "Select your employee : ";
        cout << "\n1. Manager \n2. Supervisor \n3. Exit \n\n\t : ";
        cin >> choice;
        switch (choice)
        {
            case 1:
                M.pay();
                break;
            case 2:
                S.pay();
                break;
            case 3:
                online = false;
                break;
            default:
                cout << "\nIncorrect Choice! Try Again!";
                break;
        };
        cout << "\n_____________________________________\n\n";
    }
    return 0;
}

/*
OUTPUT



*/
