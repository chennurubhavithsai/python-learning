contacts = []

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Exit")

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
        search = input("Enter contact name: ").lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == search:
                print("\n✅ Contact Found")
                print(f"Name : {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                found = True
                break

        if not found:
            print("❌ Contact not found.")

    elif choice == "4":
        update = input("Enter contact name to update: ").lower()
        found = False

        for contact in contacts:
            if contact["name"].lower() == update:
                contact["phone"] = input("Enter new phone number: ")
                contact["email"] = input("Enter new email: ")
                print("✅ Contact updated successfully!")
                found = True
                break

        if not found:
            print("❌ Contact not found.")

    elif choice == "5":
        print("Thank you for using Contact Book!")
        break

    else:
        print("❌ Invalid choice!")