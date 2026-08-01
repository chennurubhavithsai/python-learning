books = []

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

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
        print("Thank you for using Library Management System!")
        break

    else:
        print("❌ Invalid choice.")     