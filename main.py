account = {
    "name": "",
    "balance": 0.0
}

transactions = []

# Load account if it exists
try:
    with open("bank.txt", "r") as file:
        lines = file.readlines()

        if len(lines) >= 2:
            account["name"] = lines[0].strip()
            account["balance"] = float(lines[1].strip())

            for line in lines[2:]:
                transactions.append(line.strip())

except FileNotFoundError:
    pass

while True:

    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Save Account")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        account["name"] = input("Enter your name: ")
        account["balance"] = float(input("Enter initial deposit: ₹"))

        transactions.append(f"Account Created: ₹{account['balance']:.2f}")

        print("✅ Account created successfully!")

    elif choice == "2":

        if account["name"] == "":
            print("❌ Create an account first.")
        else:
            amount = float(input("Enter deposit amount: ₹"))

            account["balance"] += amount

            transactions.append(f"Deposited ₹{amount:.2f}")

            print("✅ Money deposited successfully!")

    elif choice == "3":

        if account["name"] == "":
            print("❌ Create an account first.")
        else:

            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= account["balance"]:

                account["balance"] -= amount

                transactions.append(f"Withdrew ₹{amount:.2f}")

                print("✅ Money withdrawn successfully!")

            else:

                print("❌ Insufficient balance!")

    elif choice == "4":

        if account["name"] == "":
            print("❌ No account found.")
        else:
            print("\n===== ACCOUNT DETAILS =====")
            print("Name :", account["name"])
            print(f"Balance : ₹{account['balance']:.2f}")

    elif choice == "5":

        if len(transactions) == 0:
            print("No transactions available.")
        else:
            print("\n===== TRANSACTION HISTORY =====")

            for t in transactions:
                print("-", t)

    elif choice == "6":

        with open("bank.txt", "w") as file:

            file.write(account["name"] + "\n")
            file.write(str(account["balance"]) + "\n")

            for t in transactions:
                file.write(t + "\n")

        print("✅ Account saved successfully!")

    elif choice == "7":

        print("Thank you for using Bank Management System!")
        break

    else:

        print("❌ Invalid choice.")