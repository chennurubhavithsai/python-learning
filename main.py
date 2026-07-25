students = []

# Add students
while True:
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)

    choice = input("Add another student? (yes/no): ")
    if choice.lower() != "yes":
        break

# Search student
search = input("\nEnter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == search.lower():
        print("\nStudent Found!")
        print(student)
        found = True

if not found:
    print("Student not found.")