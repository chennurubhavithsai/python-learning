account = {
    "name": "",
    "balance": 0.0
}

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account["name"] = input("Enter your name: ")
        account["balance"] = float(input("Enter initial deposit: ₹"))

        print("\n✅ Account created successfully!")
        print("Welcome,", account["name"])

    elif choice == "2":
        if account["name"] == "":
            print("❌ Please create an account first.")
        else:
            amount = float(input("Enter deposit amount: ₹"))
            account["balance"] += amount
            print(f"✅ ₹{amount:.2f} deposited successfully!")

    elif choice == "3":
        if account["name"] == "":
            print("❌ Please create an account first.")
        else:
            amount = float(input("Enter withdrawal amount: ₹"))

            if amount <= account["balance"]:
                account["balance"] -= amount
                print(f"✅ ₹{amount:.2f} withdrawn successfully!")
            else:
                print("❌ Insufficient balance!")

    elif choice == "4":
        if account["name"] == "":
            print("❌ No account found.")
        else:
            print("\n===== ACCOUNT DETAILS =====")
            print("Account Holder :", account["name"])
            print(f"Balance : ₹{account['balance']:.2f}")

    elif choice == "5":
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("❌ Invalid choice.")