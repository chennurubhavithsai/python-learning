score = 0

print("===== PYTHON QUIZ =====")

print("\nQuestion 1")
print("What is the output of print(5 + 3)?")
print("A. 53")
print("B. 8")
print("C. Error")
print("D. None")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

print("\nQuestion 2")
print("Which keyword is used to create a function?")
print("A. function")
print("B. define")
print("C. def")
print("D. func")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "C":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

print("\nQuestion 3")
print("Which data type stores True or False?")
print("A. int")
print("B. bool")
print("C. string")
print("D. list")

answer = input("Enter your answer (A/B/C/D): ").upper()

if answer == "B":
    print("✅ Correct!")
    score += 1
else:
    print("❌ Wrong!")

print("\n====================")
print("Your Score:", score, "/3")