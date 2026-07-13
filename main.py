name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

print()
print("===== Student Result =====")
print("Name:", name)
print("Marks:", marks)

if marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 50:
    print("Grade: C")

else:
    print("Grade: FAIL")