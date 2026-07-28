transactions = []

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter income amount: $"))
        transactions.append({
            "type": "Income",
            "amount": amount
        })
        print("✅ Income added successfully!")

    elif choice == "2":
        amount = float(input("Enter expense amount: $"))
        transactions.append({
            "type": "Expense",
            "amount": amount
        })
        print("✅ Expense added successfully!")

    elif choice == "3":
        if len(transactions) == 0:
            print("No transactions available.")
        else:
            print("\n===== TRANSACTIONS =====")
            for i, transaction in enumerate(transactions, start=1):
                print(f"{i}. {transaction['type']} - ${transaction['amount']:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice.")