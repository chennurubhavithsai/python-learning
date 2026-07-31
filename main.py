account = {
    "name": "",
    "balance": 0.0
}

while True:
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Check Balance")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        account["name"] = input("Enter your name: ")
        account["balance"] = float(input("Enter initial deposit: ₹"))

        print("\n✅ Account created successfully!")
        print("Welcome,", account["name"])

    elif choice == "2":
        if account["name"] == "":
            print("❌ No account found. Please create an account first.")
        else:
            print("\n===== ACCOUNT DETAILS =====")
            print("Account Holder:", account["name"])
            print("Balance: ₹", account["balance"])

    elif choice == "3":
        print("Thank you for using the Bank Management System!")
        break

    else:
        print("❌ Invalid choice.")