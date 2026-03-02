from datetime import datetime


class Transaction:
    def __init__(self, transaction_id, account_number, transaction_type, amount):

        self.transaction_id = transaction_id
        self.account_number = account_number
        self.transaction_type = transaction_type
        self.amount = amount
        self.timestamp = datetime.now()