"""Create a base class called Account with an account holder's name (string) and balance (number, like 1000.0). Use a single underscore to keep the name and balance protected.
Create a class called SavingsAccount that inherits from Account and has a method calculate_interest that returns the interest as balance * 0.05 (5% interest).
Create a class called CurrentAccount that inherits from Account and has a method calculate_interest that returns the interest as balance * 0.02 (2% interest).
Add a special method to the Account class so that using the + operator on two accounts adds their balances together.
In the main part of the program:
Create a SavingsAccount object for "Ravi" with a balance of 10000.
Create a CurrentAccount object for "Anjali" with a balance of 15000.
Show the name, balance, and interest for each account object.
Show the total balance by adding the two account objects using the + operator.
Make the output clear, showing each account’s name, balance, interest, and the total balance."""

class Account:
    def __init__(self, name, balance):
        self._name = name          
        self._balance = balance      

  
    def __add__(self, other):
        return self._balance + other._balance

   
    def display(self):
        return f"Name: {self._name}, Balance: {self._balance}"


class SavingsAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.05   


class CurrentAccount(Account):
    def calculate_interest(self):
        return self._balance * 0.02     

s1 = SavingsAccount("Ravi", 10000)
c1 = CurrentAccount("Anjali", 15000)

print(s1.display())
print("Savings Interest:", s1.calculate_interest())
print()

print(c1.display())
print("Current Interest:", c1.calculate_interest())
print()
total = s1 + c1
print("Total Balance (Ravi + Anjali):", total)


        
        