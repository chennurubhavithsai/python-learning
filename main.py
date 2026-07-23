class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("₹", amount, "deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("₹", amount, "withdrawn successfully.")
        else:
            print("Insufficient Balance!")

    def display(self):
        print("\nCurrent Balance: ₹", self.balance)


account = BankAccount("Bhavith Sai", 1000)

account.deposit(500)
account.withdraw(300)

account.display()