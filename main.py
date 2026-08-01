books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        books.append({
            "title": title,
            "author": author,
            "available": True
        })

        print("✅ Book added successfully!")

    elif choice == "2":
        if len(books) == 0:
            print("No books available.")
        else:
            print("\n===== BOOK LIST =====")
            for i, book in enumerate(books, start=1):
                status = "Available" if book["available"] else "Borrowed"
                print(f"\nBook {i}")
                print(f"Title : {book['title']}")
                print(f"Author: {book['author']}")
                print(f"Status: {status}")

    elif choice == "3":
        search = input("Enter book title: ").lower()
        found = False

        for book in books:
            if book["title"].lower() == search:
                print("\n✅ Book Found")
                print("Title :", book["title"])
                print("Author:", book["author"])
                print("Status:", "Available" if book["available"] else "Borrowed")
                found = True
                break

        if not found:
            print("❌ Book not found.")

    elif choice == "4":
        borrow = input("Enter book title to borrow: ").lower()
        found = False

        for book in books:
            if book["title"].lower() == borrow:
                found = True

                if book["available"]:
                    book["available"] = False
                    print("✅ Book borrowed successfully!")
                else:
                    print("❌ Book is already borrowed.")
                break

        if not found:
            print("❌ Book not found.")

    elif choice == "5":
        print("Thank you for using Library Management System!")
        break

    else:
        print("❌ Invalid choice.")1