class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def display(self):
        print("\n===== Account Details =====")
        print("Name:", self.name)
        print("Balance: ₹", self.balance)


account = BankAccount("Bhavith Sai", 1000)

account.display()