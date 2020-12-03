// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Student
{
protected:
    string name;
    int age;
    int reg_no;

public:
    virtual void sort(int n) = 0;
    void std_input()
    {
        cout << "Enter name: ";
        cin >> name;
        cout << "Enter Reg no. : ";
        cin >> reg_no;
        cout << "Enter age: ";
        cin >> age;
    }
    void std_output()
    {
        cout << "Name : " << name << endl;
        cout << "Age : " << age << endl;
        cout << "Reg No. : " << reg_no << endl;
    }
};

class BTech_Student : public Student
{
protected:
    int marks;

public:
    void btech_input()
    {
        std_input();
        cout << "Enter the mark: ";
        cin >> marks;
    }
    void sort(int n)
    {
        for (int i = 0; i < n - 1; ++i)
        {
            for (int j = 0; j < n - i - 1; ++j)
            {
                if (this[i].marks > this[i + 1].marks)
                {
                    BTech_Student temp = this[i];
                    this[i] = this[i + 1];
                    this[i + 1] = temp;
                }
                if (this[i].marks == this[i + 1].marks)
                {
                    if ((this[i].name.compare(this[i + 1].name)) < 0)
                    {
                        BTech_Student temp = this[i];
                        this[i] = this[i + 1];
                        this[i + 1] = temp;
                    }
                }
            }
        }
    }
    void btech_output()
    {
        std_output();
        cout << "Marks : " << marks << endl;
    }
};

class MTech_Student : public Student
{
protected:
    float gpa;

public:
    void mtech_input()
    {
        std_input();
        cout << "Enter the gpa: ";
        cin >> gpa;
    }
    void sort(int n)
    {
        for (int i = 0; i < n - 1; ++i)
        {
            for (int j = 0; j < n - i - 1; ++j)
            {
                if (this[i].gpa > this[i + 1].gpa)
                {
                    MTech_Student temp = this[i];
                    this[i] = this[i + 1];
                    this[i + 1] = temp;
                }
                if (this[i].gpa == this[i + 1].gpa)
                {
                    if ((this[i].name.compare(this[i + 1].name)) < 0)
                    {
                        MTech_Student temp = this[i];
                        this[i] = this[i + 1];
                        this[i + 1] = temp;
                    }
                }
            }
        }
    }
    void mtech_output()
    {
        std_output();
        cout << "GPA : " << gpa << endl;
    }
};

int main()
{
    Student *student;
    int n_btech, n_mtech, i;

    cout << "Enter number of BTech students : ";
    cin >> n_btech;
    BTech_Student BTECH[n_btech];

    cout << "Enter BTech Student Details\n" << "----------------------------\n";
    for (i = 0; i < n_btech; i++)
    {
        cout << "\nSTUDENT " << i + 1 << endl;
        BTECH[i].btech_input();
    }

    cout << "\n\nEnter number of MTech students : ";
    cin >> n_mtech;
    MTech_Student MTECH[n_mtech];

    cout << "Enter MTech Student Details\n" << "----------------------------\n";
    for (i = 0; i < n_mtech; i++)
    {
        cout << "\nSTUDENT " << i + 1 << endl;
        MTECH[i].mtech_input();
    }

    student = BTECH;
    student -> sort(n_btech);

    cout << "\n\nBTech Students (sorted)\n" << "----------------------\n";
    for (i = 0; i < n_btech; i++)
    {
        cout << "\nSTUDENT " << i + 1 << endl;
        BTECH[i].btech_output();
    }

    student = MTECH;
    student->sort(n_mtech);

    cout << "\n\nMTech Students (sorted)\n" << "----------------------\n";
    for (i = 0; i < n_mtech; i++)
    {
        cout << "\nSTUDENT " << i + 1 << endl;
        MTECH[i].mtech_output();
    }

    return 0;
}

/*
OUTPUT



*/
