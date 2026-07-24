class Library:

    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter Book Name: ")
        self.books.append(book)
        print("Book Added Successfully!")

    def remove_book(self):
        book = input("Enter Book Name to Remove: ")

        if book in self.books:
            self.books.remove(book)
            print("Book Removed Successfully!")
        else:
            print("Book Not Found!")

    def show_books(self):

        if len(self.books) == 0:
            print("Library is Empty!")
        else:
            print("\n===== Books =====")

            for book in self.books:
                print("-", book)


library = Library()

while True:

    print("\n===== LIBRARY MENU =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Show Books")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        library.add_book()

    elif choice == "2":
        library.remove_book()

    elif choice == "3":
        library.show_books()

    elif choice == "4":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid Choice!")