// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
#include <strings.h>

using namespace std;

class Employee
{
protected:
    int no;
    float bp, da;
    char emp_class, name[30];

public:
    float totalPay;
    void input(char emp_type)
    {
        emp_class = emp_type;
        if (emp_type == 'M')
        {
            bp = 50000;
            da = 50;
        }
        else
        {
            bp = 10000;
            da = 20;
        }
        cout << "Enter Employee No. : ";
        cin >> no;
        cout << "Enter Employee Name : ";
        cin >> name;
        totalPay = bp + (bp * da / 100);
    };
    void output()
    {
        cout << no << "\t\t " << name << "\t\t " << emp_class << "\t\t\t " << bp << "\t\t " << da << "\t\t " << totalPay << " \n";
    }
};

class Manager : public Employee
{
public:
};

class Worker : public Employee
{
public:
};

int main()
{
    Employee E[5];
    int i = 0;
    char emp_class;

    while (i < 5)
    {
        cout << "Enter Employee " << i + 1 << " details : \n";
        cout << "Enter employee class (M for Manager & W for Worker) : ";
        cin >> emp_class;
        if (emp_class == 'M' || emp_class == 'm')
        {
            E[i].input('M');
            i++;
        }
        else if (emp_class == 'W' || emp_class == 'w')
        {
            E[i].input('W');
            i++;
        }
        else
        {
            cout << "Invalid employee type ! Try Again !\n";
        }
    }

    for (int i = 0; i < 5; ++i)
    {
        for (int j = 0; j < 5 - i; ++j)
        {
            if (E[j].totalPay > E[j + 1].totalPay)
            {
                Employee temp = E[j];
                E[j] = E[j + 1];
                E[j + 1] = temp;
            }
        }
    }

    cout << "\nNo \t\t Name \t\t Class(M/W) \t\t BP \t\t DA \t\t Total Pay";
    cout << "\n*************************************************";
    cout << "*************************************************\n";
    for (i = 0; i < 5; i++)
    {
        E[i].output();
    }

    return 0;
}
