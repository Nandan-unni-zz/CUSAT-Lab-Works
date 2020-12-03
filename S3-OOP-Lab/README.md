# S3 Object Oriented Programming Lab
Solutions to the III Semester OOP Lab Programs, 2019 Scheme <br /><br />

**1.** A phone number, such as (212) 767-8900, can be thought of as having three parts: the area code (212), the exchange (767), and the number (8900). Write a C++ program that uses a structure to store these three parts of a phone number separately. Call the structure phone. Create two structure variables of type phone. Initialize one, and have the user input a number for the other one. Then display both numbers.<br /><br />

**2.** Define a class Date that contains details like year, month and date. Write a C++ program to check the validity of the date that you enter and display the next date.<br /><br />

**3.** Define a class to represent a bank account. Include members like name of depositor, account  no, Type of account, balance amount in the account. Write C++ program with member functions to a) Assign initial values b) To deposit an account c) To withdraw an amount after checking the balance d) To display name and balance <br /><br />

**4.** Write a class which represents the shape triangle. The member functions should a) Check the validity of the triangle b) display the sides c) find the area and display it.<br /><br />

**5.** Write  class which contains an integer array and a static function to find the average of that array. Create three objects. Read the values into the array using one object, and find the average. Let the second object modifies the value by multiplying each element by a certain multiplier. Repeat the process of finding the average usng first object. Using the third object arrange the numbers in ascending order and print. <br /><br />

**6.** Write a program to find shortest distance between three coordinates points, representing vertices of a triangle, using inline function. Also check the validity of the sides to make a triangle. <br /><br />

**7.** Write a function called swap() that interchanges two int values 	belonging to an object, passed as parameter to it by the calling program. Write a C++ program to demonstrate call by value, call by reference and call by address. <br /><br />

**8.** Write a function called power() that takes a double value for n and an int value for p, and returns the result as a double value. Create a series of overloaded functions with the same name that, in addition to double, also work with types char, int, long, and float. Write a main() program that exercises these overloaded functions with all argument types. <br /><br />

**9.** Define a class Date. Overload the operator '+' such that it adds a given date with certain number of days. <br /><br />

**10.** Distance is measured in feet and inches unit. Use operator overloading for '+' operator for adding two such distances and '<' for comparing two such distances. (One of the operator function should be implemented as friend function.) <br /><br />

**11.** Write a program using operator overloading to overload Stream operators (<< and >>) to read and display the objects of complex class. <br /><br />

**12.** A class representing distance is measured in the unit of feet and inches. Write a program to do conversion from meter unit to objects of class type and objects of class type to meter. <br /><br />

**13.** Polar coordinates are represented in angle and radius format while rectangular coordinates represented as (x,y). Define classes for both types and include member functions to convert from polar to rectangular coordinates. (conversion from class to class.) <br /><br />

**14.** Employee class contain details like name, emp no, pay rate, constructor function and a pay() function. Manager class inherits from employee and has the option of drawing pay on hourly basis or salary basis and has an additional data issalaried(bool). Class Supervisor is derived from employee and has an additional field department and is always salaried. Base and both derived classes should contain pay() function with same name. <br /><br />

**15.** Write a C++ program to create a class Student with age, name and register number. Using Inheritance, derive two classes MTech-stud and BTech-stud List both the category of students in the increasing order of marks (for BTech-stud) and gpa (for MTech-stud). In case of tie, display whichever name comes first. Make sort() function as a virtual function. <br /><br />

**16.** Implement the base class Shape and derive triangle,rectangle,circle and square classes from it. Implement functions to compute the area and perimeter of the polygon. Use the concept of pure virtual functions. <br /><br />
