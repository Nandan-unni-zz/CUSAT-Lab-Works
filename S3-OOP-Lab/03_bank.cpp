// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Bank
{
private:
    string acc_name, acc_type;
    int acc_no, balance;

public:
    void init()
    {
        cout << "Enter the Account Name : ";
        cin >> acc_name;
        cout << "Enter the Account Type : ";
        cin >> acc_type;
        cout << "Enter the Initial Balance : ";
        cin >> balance;
    }
    void deposit()
    {
        int amount;
        cout << "Enter the amount to deposit : ";
        cin >> amount;
        balance += amount;
        cout << "Balance : " << balance << "\n";
    }
    void withdraw()
    {
        int amount;
        cout << "Balance : " << balance << "\n";
        cout << "Enter the amount to withdraw : ";
        cin >> amount;
        if (amount < balance)
            balance -= amount;
        else
            cout << "Insufficient Balance\n";
        cout << "Balance : " << balance << "\n";
    }
    void details()
    {
        cout << "Account Name : " << acc_name;
        cout << "\nBalance : " << balance << "\n";
    }
} b;

int main()
{
    int choice;
    bool online = true;
    cout << "\nCreate Account \n";
    b.init();
    while (online)
    {
        cout << "\n\n 1. Deposit Money \t 2. Withdraw Money \n\n 3. Account Details \t 4. Exit \n\n\t Enter choice : ";
        cin >> choice;
        switch (choice)
        {
        case 1:
            cout << "\nDEPOSIT MONEY \n";
            b.deposit();
            break;
        case 2:
            cout << "\nWITHDRAW MONEY \n";
            b.withdraw();
            break;
        case 3:
            cout << "\nACCOUNT DETAILS \n";
            b.details();
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

Create Account 
Enter the Account Name : Nandanunni
Enter the Account Type : Savings
Enter the Initial Balance : 1000


 1. Deposit Money        2. Withdraw Money 

 3. Account Details      4. Exit 

         Enter choice : 2

WITHDRAW MONEY 
Balance : 1000
Enter the amount to withdraw : 2000
Insufficient Balance
Balance : 1000


 1. Deposit Money        2. Withdraw Money 

 3. Account Details      4. Exit 

         Enter choice : 1

DEPOSIT MONEY 
Enter the amount to deposit : 3000
Balance : 4000


 1. Deposit Money        2. Withdraw Money 

 3. Account Details      4. Exit 

         Enter choice : 2

WITHDRAW MONEY 
Balance : 4000
Enter the amount to withdraw : 2000
Balance : 2000


 1. Deposit Money        2. Withdraw Money 

 3. Account Details      4. Exit 

         Enter choice : 3

ACCOUNT DETAILS 
Account Name : Nandanunni
Balance : 2000


 1. Deposit Money        2. Withdraw Money 

 3. Account Details      4. Exit 

         Enter choice : 4

*/