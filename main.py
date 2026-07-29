contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")

        contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        print("✅ Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n===== CONTACT LIST =====")
            for i, contact in enumerate(contacts, start=1):
                print(f"\nContact {i}")
                print(f"Name : {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice.")