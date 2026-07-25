students = [
    {
        "name": "bhavith sai",
        "age": "17",
        "course": "MPC"
    },
    {
        "name": "efrahem",
        "age": "16",
        "course": "BiPC"
    }
]

update_name = input("\nEnter student name to update: ")

found = False

for student in students:
    if student["name"].lower() == update_name.lower():
        print("\nStudent Found!")

        student["age"] = input("Enter new age: ")
        student["course"] = input("Enter new course: ")

        print("\nStudent Updated Successfully!")
        found = True
        break

if not found:
    print("Student not found.")

print("\n===== Updated Records =====")
for student in students:
    print(student)