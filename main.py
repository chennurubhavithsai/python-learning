student = {}

student["name"] = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))
student["course"] = input("Enter your course: ")

print("\n===== Student Information =====")

for key, value in student.items():
    print(key.capitalize() + ":", value)