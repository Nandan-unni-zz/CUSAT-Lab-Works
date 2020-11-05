// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <iostream>
using namespace std;

class Average
{
    public:
        int arr[25], average;
        void input(int n)
        {
            cout << "\nEnter the elements of the array : ";
            for (int i = 0; i < n; i++)
                cin >> arr[i];
        }
        void output(int n)
        {
            cout << "\nThe array is [";
            for (int i = 0; i < n; i++)
                cout << arr[i] << ", ";
            cout << "] \nThe average is " << average << endl;
        }
        int static getAverage(int *ptr, int n, int multiplier = 1)
        {
            int sum=0, avg;
            for (int i = 0; i < n; i++)
            {
                *(ptr + i) *= multiplier;
                sum += *(ptr + i);
            }
            avg = sum / n;
            return avg;
        }
        void sort(int *ptr, int n)
        {
            int i, j;    
            int temp=0;            
            for(i = 0; i < n-1; i++)
            {
                for (j = 0; j < n-1; j++)
               {
                   if (*(ptr + j) > *(ptr +(j+1)))      
                   { 
                    temp = *(ptr + j);             
                    *(ptr + j) = *(ptr +(j+1));
                    *(ptr +(j+1)) = temp;               
                   }
               }
            }
            cout << "\nArray sorted in ascending order !\n";
        }
} obj1, obj2, obj3;

int main()
{
    int n, multiplier;
    cout << "\nEnter the number of elements of array : ";
    cin >> n;
    obj1.input(n);
    obj1.average = obj1.getAverage(&obj1.arr[0], n);
    obj1.output(n);
    obj2 = obj1;
    cout << "\nEnter the multiplier for the second array : ";
    cin >> multiplier;
    obj2.average = obj2.getAverage(&obj2.arr[0], n, multiplier);
    obj2.output(n);
    obj3 = obj1;
    obj3.sort(&obj3.arr[0], n);
    obj3.output(n);
    return 0;
}

/*
OUTPUT



*/
