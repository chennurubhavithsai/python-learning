books = [
    "Python Basics",
    "Data Structures",
    "Machine Learning"
]

new_book = input("Enter a new book: ")
books.append(new_book)

remove_book = input("Enter a book to remove: ")

if remove_book in books:
    books.remove(remove_book)
    print("Book removed successfully!")
else:
    print("Book not found!")

print("\n===== Updated Library =====")

for book in books:
    print(book)