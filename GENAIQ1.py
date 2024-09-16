#PRN:21070521035 NAME:Kashish Sharma
import random

class BankAccount:
    def __init__(self, account_id, balance=0):
        self.account_id = account_id
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposit: {amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: {amount}")
        else:
            self.transactions.append(f"Withdrawal Failed: Insufficient funds")

    def __repr__(self):
        return f"Account ID: {self.account_id}, Final Balance: {self.balance}, Transactions: {len(self.transactions)}"

def generate_accounts(num_accounts, num_months, seed):
    random.seed(seed)
    accounts = []
    
    for i in range(num_accounts):
        initial_balance = random.randint(1000, 5000)
        account = BankAccount(account_id=i+1, balance=initial_balance)
        
        for month in range(num_months):
            num_transactions = random.randint(1, 10)
            for _ in range(num_transactions):
                transaction_type = random.choice(['deposit', 'withdraw'])
                amount = random.randint(100, 1000)
                
                if transaction_type == 'deposit':
                    account.deposit(amount)
                elif transaction_type == 'withdraw':
                    account.withdraw(amount)
        
        accounts.append(account)
    
    accounts.sort(key=lambda x: x.balance)
    
    return accounts

num_accounts = 100
num_months = 6
seed_value = 42
accounts = generate_accounts(num_accounts, num_months, seed_value)

for account in accounts:
    print(account)
