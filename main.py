books = []

# Load books from file
try:
    with open("library.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 3:
                books.append({
                    "title": data[0],
                    "author": data[1],
                    "available": data[2] == "True"
                })

except FileNotFoundError:
    pass


while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Save Library")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")

        books.append({
            "title": title,
            "author": author,
            "available": True
        })

        print("✅ Book Added Successfully!")

    elif choice == "2":

        if len(books) == 0:
            print("No books available.")

        else:

            print("\n===== BOOK LIST =====")

            for i, book in enumerate(books, start=1):

                status = "Available" if book["available"] else "Borrowed"

                print(f"\nBook {i}")
                print("Title :", book["title"])
                print("Author:", book["author"])
                print("Status:", status)

    elif choice == "3":

        search = input("Enter Book Title: ").lower()

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
            print("❌ Book Not Found")

    elif choice == "4":

        borrow = input("Enter Book Title to Borrow: ").lower()

        found = False

        for book in books:

            if book["title"].lower() == borrow:

                found = True

                if book["available"]:
                    book["available"] = False
                    print("✅ Book Borrowed Successfully!")
                else:
                    print("❌ Book Already Borrowed!")

                break

        if not found:
            print("❌ Book Not Found")

    elif choice == "5":

        return_book = input("Enter Book Title to Return: ").lower()

        found = False

        for book in books:

            if book["title"].lower() == return_book:

                found = True

                if not book["available"]:
                    book["available"] = True
                    print("✅ Book Returned Successfully!")
                else:
                    print("❌ This Book Was Not Borrowed.")

                break

        if not found:
            print("❌ Book Not Found")

    elif choice == "6":

        with open("library.txt", "w") as file:

            for book in books:

                file.write(
                    f"{book['title']},{book['author']},{book['available']}\n"
                )

        print("✅ Library Saved Successfully!")

    elif choice == "7":

        print("📚 Thank You For Using Library Management System!")
        break

    else:

        print("❌ Invalid Choice")