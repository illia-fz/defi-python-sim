# Simple DeFi simulation in Python

class DeFiBank:
    def __init__(self, interest_rate=0.05):
        self.balances = {}
        self.interest_rate = interest_rate

    def deposit(self, user, amount):
        self.balances[user] = self.balances.get(user, 0) + amount
        print(f"{user} deposited {amount} ETH. Balance: {self.balances[user]} ETH")

    def withdraw(self, user, amount):
        if self.balances.get(user, 0) >= amount:
            self.balances[user] -= amount
            print(f"{user} withdrew {amount} ETH. Balance: {self.balances[user]} ETH")
        else:
            print("Insufficient balance")

    def accrue_interest(self):
        for user in self.balances:
            interest = self.balances[user] * self.interest_rate
            self.balances[user] += interest
            print(f"Interest accrued for {user}: {interest} ETH")


if __name__ == '__main__':
    bank = DeFiBank(interest_rate=0.1)
    bank.deposit('Alice', 10)
    bank.deposit('Bob', 5)
    bank.accrue_interest()
    bank.withdraw('Alice', 3)
