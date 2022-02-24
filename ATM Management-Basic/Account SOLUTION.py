class Account:
    def __init__(self, no, name, bal):
        self.no = no
        self.name = name
        self.bal = bal
    def deposit(self, depamnt):
        self.depamnt = depamnt
        self.bal = self.bal + self.depamnt
        return self.bal
    def withdraw(self, withdrawamnt):
        self.withdrawamnt = withdrawamnt
        if self.bal>1000 or self.bal==1000:
            self.bal = self.bal - self.withdrawamnt
            return self.bal
        else:
            return "insuficient"

no = int(input())
name = input()
bal = int(input())

depamnt = int(input())
withdrawamnt = int(input())

res1 = Account(no, name, bal)
res2 = Account(no, name, bal)

print(res1.deposit(depamnt))
print(res2.withdraw(withdrawamnt))
