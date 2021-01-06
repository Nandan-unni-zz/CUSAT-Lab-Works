// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

struct Phone
{
    int area_code, exchange_code, num_code;
    void disp_number()
    {
        cout << '(' << area_code << ") " << exchange_code << '-' << num_code << "\n";
    }
};

int main()
{
    Phone phno1, phno2;
    phno1.area_code = 212;
    phno1.exchange_code = 767;
    phno1.num_code = 8900;
    cout << "Enter your area code, exchange and number: ";
    cin >> phno2.area_code >> phno2.exchange_code >> phno2.num_code;
    cout << "My number is ";
    phno1.disp_number();
    cout << "Your number is ";
    phno2.disp_number();
    return 0;
}

/*
OUTPUT

Enter your area code, exchange and number: 415 555 1212
My number is (212) 767-8900
Your number is (415) 555-1212

*/