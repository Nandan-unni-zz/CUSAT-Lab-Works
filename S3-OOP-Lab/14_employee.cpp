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
        cout << "\nSelect Manager's Pay Method : ";
        cout << "\n1. Hourly Basis \n2. Salary Basis \n\n\t : ";
        int choice;
        cin >> choice;
        if (choice == 1)
            issalaried = false;
        else if (choice == 2)
            issalaried = true;
        else
            issalaried = true;
        if (issalaried)
            cout << "\nPay Method : Salary Basis\n";
        else
            cout << "\nPay Method : Hourly Basis\n";
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
    cout << "Enter MANAGER details \n";
    Manager M;
    cout << "\n\nEnter SUPERVISOR details \n";
    Supervisor S;
    while (online)
    {
        cout << "\n_____________________________________\n\n";
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
    }
    return 0;
}

/*
OUTPUT

Enter MANAGER details 

Enter the name of the Employee: Nandan
Enter the Employee Number: 20219023
Enter the Pay Rate: 100

Select Manager's Pay Method : 
1. Hourly Basis 
2. Salary Basis 

         : 1

Pay Method : Hourly Basis


Enter SUPERVISOR details 

Enter the name of the Employee: Unni
Enter the Employee Number: 23
Enter the Pay Rate: 10000

Enter the department: CS

_____________________________________

Select your employee : 
1. Manager 
2. Supervisor 
3. Exit 

         : 1

Enter the no of hours worked: 50
Amount Paid : 5000
_____________________________________

Select your employee : 
1. Manager 
2. Supervisor 
3. Exit 

         : 2

Pay rate : 10000
_____________________________________

Select your employee : 
1. Manager 
2. Supervisor 
3. Exit 

         : 3

*/
