class Account():
    def __init__(self, acc_number, bal, bank):
        self.acc_number = acc_number
        self.balance = bal
        self.bank = bank

    def bal_check(self):
        return f"This {self.bank} account has a balance of ${self.bal}"
    
    def deposit(self, amnt):
        self.bal = self.bal + amnt
        return f"Credit Alert:\nThe sum of ${amnt} has been deposited into your account\nNew Bal: ${self.bal}"
    
acc_1 = Account("2179094505", 0.23, "UBA")

print(f"Initial Bal: ${acc_1.balance}\n")

# print(acc_1.deposit(26))
