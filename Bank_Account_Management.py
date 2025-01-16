class Bank:
#create a bank class where the account number, name, and balance is stored.
    def __init__(self, balance, account_number):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = account_number

#deposit function when the amount is added
    def deposit(self, amount):
        self.balance += amount
#withdraw funtion where the amount is withdrawn
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds.")

    def get_account_holder(self):
        return self.account_holder

    def get_balance(self):
        return self.balance

    def get_account_number(self):

        return self.account_number


    def set_account_number(self, account_number):
        self.account_number = account_number
  
    def monthly_process(self):
        pass

    def __str__(self):
        return f"{self.account_number}  {self.account_holder}  {self.balance:.2f}"

#since bank is the parent class we will use it in Savingaccount and checkingaccount to gain the stored information 
class SavingsAccount(Bank):
    INTEREST_RATE = 0.01

    def __init__(self, account_number, account_holder, balance, interest_rate=INTEREST_RATE):
        super().__init__(balance, account_number)
        self.interest_rate = interest_rate
        self.status = True
    def get_interest_rate(self):
        return self.interest_rate

    def set_interest_rate(self, interest_rate):
        self.interest_rate = interest_rate

    def calc_interest(self):
        self.deposit(self.get_balance() * self.interest_rate / 12)
        self.monthly_process()

    def __str__(self):
        return f"{super().__str__()}  {self.interest_rate}"

#set a maximum amount of check that can be stored and the service fee for extra checks
class CheckingAccount(Bank):
    MaxNumChecks = 10
    ServiceFee = 10.0

    def __init__(self, account_number, account_holder, balance, service_charges=0):
        super().__init__(balance, account_number)
        self.service_charges = service_charges
        self.numchecks = 0

    def get_service_charges(self):
        return self.service_charges

    def set_service_charges(self, service_charges):
        self.service_charges = service_charges

    def monthly_process(self):
        if self.numchecks > CheckingAccount.MaxNumChecks:
            val = (self.numchecks - CheckingAccount.MaxNumChecks) * self.service_charges
            self.withdraw(val)
        self.numchecks= 0

    def write_check(self, check):
        self.withdraw(check)
        self.numchecks += 1

    def __str__(self):
        return f"{super().__str__()}  {self.numchecks}"



print("Welcome to the Bank. We will begin the registration for your new account.")

# ceate a savings account to recall from the class
account_number = input("Please enter your pin number for savings account: ")
account_holder= input("Please enter your name for savings account: ")
balance = float(input("Enter how much you would like to put into your savings account: $"))
savings_account = SavingsAccount(account_number, account_holder, balance)

# create a checking account to recall from the class
account_number = input("Please enter your pin number for checkings account: ")
account_holder = input("Please enter your name for checkings account: ")
balance = float(input("Enter how much you would like to put into your checkings account: $"))
checking_account = CheckingAccount(account_number, account_holder, balance)

#provide options for the user to recall the functions from the class
while True:
    print("Please select the purpose of your visit:")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Calculate interest on SavingsAccount")
    print("4. Write a check")
    print("5. Display account details")
    print("6. Return to exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter the amount you would like to deposit: $"))
        savings_account.deposit(amount)
        checking_account.deposit(amount)
        print("Your deposit is successfully completed.")
    elif choice == "2":
        amount = float(input("Enter the amount you would like to withdraw: $"))
        savings_account.withdraw(amount)
        checking_account.withdraw(amount)
        print("Your withdrawal is successfully completed.")
    elif choice == "3":
        if isinstance(savings_account, SavingsAccount):
            savings_account.calc_interest()
            print("Your total amount now including interest is: ")
        else:
            print("Invalid choice.")
    elif choice == "4":
        if isinstance(checking_account, CheckingAccount):
            check_amount = float(input("Enter the check amount: "))
            checking_account.write_check(check_amount)
            print("The check has been written successfully.")
        else:
            print("Invalid choice. ")
    elif choice == "5":
        print("\nSavings Account Details:")
        print(savings_account)
        print("\nChecking Account Details:")
        print(checking_account)
    elif choice == "6":
        print("Have a nice day!")
        break
    else:
        print("Invalid choice")
