name = input("Enter your name: ")
course = input("Enter your course: ")

file = open("student.txt", "w")

file.write("Name: " + name + "\n")
file.write("Course: " + course)

file.close()

print("\nData Saved Successfully!")

file = open("student.txt", "r")

print("\n===== Student Details =====")
print(file.read())

file.close()