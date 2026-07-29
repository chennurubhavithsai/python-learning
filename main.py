contacts = []

# Load contacts from file
try:
    with open("contacts.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 3:
                contacts.append({
                    "name": data[0],
                    "phone": data[1],
                    "email": data[2]
                })
except FileNotFoundError:
    pass

while True:

    print("\n===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Save Contacts")
    print("7. Exit")

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

        print("✅ Contact Added Successfully!")

    elif choice == "2":

        if len(contacts) == 0:
            print("No Contacts Found!")

        else:
            print("\n===== CONTACT LIST =====")

            for i, contact in enumerate(contacts, start=1):
                print(f"\nContact {i}")
                print(f"Name : {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")

    elif choice == "3":

        search = input("Enter Name: ").lower()

        found = False

        for contact in contacts:

            if contact["name"].lower() == search:

                print("\n✅ Contact Found")
                print(contact)

                found = True
                break

        if not found:
            print("❌ Contact Not Found")

    elif choice == "4":

        update = input("Enter Contact Name: ").lower()

        found = False

        for contact in contacts:

            if contact["name"].lower() == update:

                contact["phone"] = input("Enter New Phone: ")
                contact["email"] = input("Enter New Email: ")

                print("✅ Contact Updated Successfully!")

                found = True
                break

        if not found:
            print("❌ Contact Not Found")

    elif choice == "5":

        delete = input("Enter Contact Name to Delete: ").lower()

        found = False

        for contact in contacts:

            if contact["name"].lower() == delete:

                contacts.remove(contact)

                print("✅ Contact Deleted Successfully!")

                found = True
                break

        if not found:
            print("❌ Contact Not Found")

    elif choice == "6":

        with open("contacts.txt", "w") as file:

            for contact in contacts:

                file.write(
                    f"{contact['name']},{contact['phone']},{contact['email']}\n"
                )

        print("✅ Contacts Saved Successfully!")

    elif choice == "7":

        print("Thank You For Using Contact Book!")
        break

    else:

        print("❌ Invalid Choice")