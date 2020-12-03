// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

bool leap_year_check(int year)
{
    if (((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0))
        return true;
    else
        return false;
}

class Date
{
    private:
        int day, month, year;
        bool is_leap_year = false;
    public:
        void input()
        {
            cout << "Enter the day, month and year : ";
            cin >> day >> month >> year;
            is_leap_year = leap_year_check(year);
        }

        void output()
        {
            cout << endl << day << " / " << month << " / " << year << endl;
        }

        bool is_valid()
        {
            if ((day < 0) || (month < 0) || (year < 0) || (day > 31) || (month > 12))
                return false;
            
            switch (month)
            {
                case 1:
                case 3:
                case 5:
                case 7:
                case 8:
                case 10:
                case 12:
                    if (day > 31)
                        return false;
                    break;

                case 4:
                case 6:
                case 9:
                case 11:
                    if (day > 30)
                        return false;
                    break;
                
                case 2:
                    if ((is_leap_year) && (day > 29)) // leap year check
                        return false;
                    else if ((day > 28) && (!is_leap_year)) // non-leap year check
                        return false;
                    break;

                default:
                    break;
            }
            return true;
        }

        Date operator +(int days_count)
        {
            Date d2;
            d2.day = day;
            d2.month = month;
            d2.year = year;
            d2.is_leap_year = is_leap_year;

            if (days_count > 1461)
            {
                d2.year += 4 * (days_count / 1461);
                days_count = days_count % 1461;
            } // There will be 1461 days between every 4 years

            for (int i=0; i < days_count; i++)
            {
                d2.is_leap_year = leap_year_check(d2.year);
                switch (d2.month)
                {
                    case 1:
                    case 3:
                    case 5:
                    case 7:
                    case 8:
                    case 10:
                        if (d2.day < 31)
                            d2.day += 1;
                        else
                        {
                            d2.day = 1;
                            d2.month += 1;
                        }
                        break;

                    case 4:
                    case 6:
                    case 9:
                    case 11:
                        if (d2.day < 30)
                            d2.day += 1;
                        else
                        {
                            d2.day = 1;
                            d2.month += 1;
                        }
                        break;
                    
                    case 2:
                        if ((d2.day < 29) && (d2.is_leap_year))
                            d2.day += 1;
                        else if ((d2.day < 28) && (!d2.is_leap_year))
                            d2.day += 1;
                        else
                        {
                            d2.day = 1;
                            d2.month = 3;
                        }
                        break;
                    
                    case 12:
                        if (d2.day < 31)
                            d2.day += 1;
                        else
                        {
                            d2.day = 1;
                            d2.month = 1;
                            d2.year += 1;
                        }
                        break;

                    default:
                        break;
                }
            }
            return d2;
        }
};

int main()
{
    Date first, second;
    int days_count;
    first.input();
    cout << "\nThe date you entered is ";
    first.output();
    if (first.is_valid())
    {
        cout << "\nValid Date\n";
        cout << "\nEnter the no of days to be added : ";
        cin >> days_count;
        second = first + days_count;
        first.output();
        cout << " + " << days_count << " days = ";
        second.output();
    }
    else
        cout << "\nInvalid Date\n";
    return 0;
}

/*
OUTPUT



*/
