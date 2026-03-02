class Account:
    def __init__(self, account_number, customer_id, account_type, balance):
        self.account_number = account_number
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            print("Invalid Entry")
        else:
            self.balance = self.balance + amount
            print(f"Rs:{amount} is Credited to your bank account",
                  f"\nAvl Bal Rs:{self.balance}")
        

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid Entry")
        elif (self.balance - amount) <= 0 :
            print("Insufficient Balance")
        else:
            self.balance = self.balance - amount
            print(f"Rs:{amount} is Debited from your bank account",
                  f"\nAvl Bal Rs:{self.balance}")
            
    def check_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")
        
pass

a1 = Account(1,1,"s",0)



pass