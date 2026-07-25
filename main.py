students = []

while True:
    name = input("Enter student name: ")
    age = input("Enter student age: ")
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

print("\n===== Student Records =====")

for student in students:
    print(student)