Hey Everyone,
This is my first Project on Python GUI.

Start Date :- 10-05-2023
End Date :- 16-05-2023

About This Project :-
This Project is a Simple Demonstration on how a Bank Management Software works.
It contains the Basic functionalities of an ATM like Checking of Current Balance, Changing PIN Number, Withdrawal and Deposit of Money, Transfer of Money to someone else A/C and To view Transection history of your A/C.

For Sample use 
A/C      PIN
10001    1111
10002    2222
10003    3333
10004    4444
10005    5555

Front-End of this project is made using Tkinter Module of Python Programming Language.

The name of first and main window is "root", which asks the existing user to enter their A/C number and PIN number to access their A/C and perform the function required by them, and the New user to create their A/C. 

The "menu" function contains the defination of all the function mentioned above.

The "check" function checks the A/C number and PIN number which was entered by the user on "root" window.

The "acno" function generates the A/C number for a new customer.

The "newac" function displays a form for creating new A/C.

The Back-End for this program is created on MySQL. Name of Data Base is trustbank which contains two table "cust" and "history".

The table "cust" contains all the information of Customer of the TrustBank.

acno 		- 	int 		- primary key
name 		- 	char(30) 	- not null
pin 		- 	char(4) 	- not null
address 	- 	char(100) 	- 
city 		- 	char(20) 	- not null
state 		- 	char(20) 	- not null
pincode 	- 	char(10) 	- not null
phone 		- 	char(10) 	- not null
gender 		- 	char(1) 	- not null
dob 		- 	date 		- not null
occupation 	- 	char(20) 	- not null
balance 	- 	int 		- 

The table "history" contains all the transection history of all the customers.

acno		-	int
descr		-	char(100)
date		-	date
time		-	time
withdrawals	-	int
deposits	-	int
r_acno		-	int
transfer_amt	-	int
balance		-	int

