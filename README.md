# Bank-Account-Management
This is mini program demonstrates Object-Oriented Programing since this is based of a real world events. The Class functions help with reducing the amount of code that is written.
It consists of Object atrributes such as the account number and object methods where it defines the purpose of the account number. 
This bank program has one of the princple of OOP, inheritence in which we inherited the information from Class Bank into the other class functions.
The program starts with a welcome message and then asks for user input for a PIN. The number then is taken to the Bank Class which stores the number in account_number. 

The class bank has many attributes and functions, the account_holder, account_number, deposit, withdrawal, and balance. The program then asks for the name of the account which is then stored in account_holder. The deposit function is defined where when the amount is added to the balance. The withdrawal function subtracts the amount from the balance. 

The SavingsAccount has the parent function Bank in it to use the information that is stored in it. The super() function gives access to the properties of the Class Bank. The interest rate is set to 0.01 and then we set the interest rate. The function calc_interest then calculates the interest rate annually based on the savings account balance. 

The CheckinAccount has the parent function Bank in it as well and similarly, we used the super() function to give access. The maximum number of checks that can be stored in a checking account is 10 and the charge fee is 10.0 if the checks exceed the maximum number. Every time we add a check, the self.numchecks increases by 1. 


The following functions are input function function that recalls the def function from class back. Based on the input choices, the function is called back. 
