""" Identify 3 classes that might be needed for a system developed for a Bank and create them using Python.

For example: Bank: CheckingAccount, SavingAccount, Employee.

Hint: Using pass keyword for the class body in this project """


class Account:
    pass
'''
    def __init__(self, acc_number, acc_holder, balance, acc_type):
        self.acc_number = acc_number
        self.acc_holder = acc_holder
        self.balance = balance
        self.acc_type = acc_type

    def deposit(self, amount):
        pass
        #self.balance += amount

    def withdrawl(self, amount):
        pass
        #if amount <= self.balance:
            #self.balance -= amount
        #else:
            #print("Insufficient funds")

    def get_balance(self):
        pass
        #return self.balance
'''


class CheckingAccount:
    pass


class Customer:
    pass
'''
    def __init__(self, customer_id, name, phone_num):
        self.customer_id = customer_id
        self.name = name
        self.phone_num = phone_num
        self.accounts = []

    def add_account(self, account):
        pass
        #self.accounts.append(account)

    def remove_account(self, account):
        pass
        #if account in self.accounts:
            #self.accounts.remove(account)
'''


class Employee:
    pass
'''
    #attribute
    def __init__(self, employee_id, name, role):
        self.employee_id = employee_id
        self.name = name
        self.role = role
    #method
    def generate_report(self):
        pass
'''


class SavingAccount:
    pass


class Transaction:
    pass
'''
    def __init__(self, transaction_id, sender_account, reciever_account, amount, transaction_type):
        self.transaction_id = transcation_id
        self.timestamp = datetime.now()
        self.sender_account = sender_account
        self.reciever_account = reciever_account
        self.amount = amount
        self.transaction_type = transaction_type

    def get_transaction_details(self):
        pass
'''






    
