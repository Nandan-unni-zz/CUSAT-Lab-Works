// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Date
{
    private:
        int day, month, year, nxt_day, nxt_month, nxt_year;
        bool is_leap_year = false;
    public:
        void intake()
        {
            cout << "Enter the day, month and year : ";
            cin >> day >> month >> year;
            if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0))
                is_leap_year = true;
        }
        void verify_and_calc()
        {
            string status = "Valid date";
            nxt_year = year;
            nxt_month = month;
            nxt_day = day;

            if ((day < 0) || (month < 0) || (year < 0) || (day > 31) || (month > 12))
                status = "Invalid date";
            
            switch (month)
            {
                case 1:
                case 3:
                case 5:
                case 7:
                case 8:
                case 10:
                    if (day > 31)
                        status = "Invalid date";
                    else
                    {
                        if (day < 31)
                            nxt_day += 1;
                        else
                        {
                            nxt_day = 1;
                            nxt_month += 1;
                        }
                        
                    }
                    
                    break;

                case 4:
                case 6:
                case 9:
                case 11:
                    if (day > 30)
                        status = "Invalid date";
                    else
                    {
                        if (day < 30)
                            nxt_day += 1;
                        else
                        {
                            nxt_day = 1;
                            nxt_month = 5;
                        }
                        
                    }
                    break;
                
                case 2:
                    if ((is_leap_year) && (day > 29)) // leap year check
                        status = "Invalid date";
                    else if ((day > 28) && (!is_leap_year)) // non-leap year check
                        status = "Invalid date";
                    else
                    {
                        if ((day < 29) && (is_leap_year))
                            nxt_day += 1;
                        else if ((day < 28) && (!is_leap_year))
                            nxt_day += 1;
                        else
                        {
                            nxt_day = 1;
                            nxt_month = 3;
                        }
                        
                    }
                    
                    break;
                
                case 12:
                    if (day > 31)
                        status = "Invalid date";
                    else
                    {
                        if (day < 31)
                            nxt_day += 1;
                        else
                        {
                            nxt_day = 1;
                            nxt_month += 1;
                            nxt_year += 1;
                        }
                        
                    }
                    
                    break;

                default:
                    break;
            }


            cout << "\n" << status << "\n";

            if ( status == "Invalid date" )
                exit(0);

            else
            {
                cout << "Input date : " << day << " / " << month << " / " << year << "\n";
                cout << "Next date : " << nxt_day << " / " << nxt_month << " / " << nxt_year << "\n";
            }
        }
};

int main()
{
    Date d;
    d.intake();
    d.verify_and_calc();
    return 0;
}

/*
OUTPUT 1:
Enter the day, month and year : 02 03 1990

Valid date
Input date : 2 / 3 / 1990
Next date : 3 / 3 / 1990

OUTPUT 2:
Enter the day, month and year : 29 02 1989

Invalid date


*/