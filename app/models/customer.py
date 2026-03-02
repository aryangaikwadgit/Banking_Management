class Customer:
    def __init__(self,name,phone,email,customer_id):
        self.name = name
        self.phone = phone
        self.email = email
        self.customer_id = customer_id 
        self.accounts = []

    def add_account(self,acc):
        self.accounts.append(acc)


