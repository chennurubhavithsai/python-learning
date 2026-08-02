students = []

while True:
    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")

        marks = []

        for i in range(1, 6):
            mark = float(input(f"Enter marks for Subject {i}: "))
            marks.append(mark)

        total = sum(marks)
        average = total / 5
        percentage = average

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        students.append({
            "name": name,
            "marks": marks,
            "total": total,
            "average": average,
            "percentage": percentage,
            "grade": grade
        })

        print("✅ Student result added successfully!")

    elif choice == "2":

        if len(students) == 0:
            print("No student records found.")

        else:
            print("\n===== STUDENT RESULTS =====")

            for student in students:
                print("\nName:", student["name"])
                print("Marks:", student["marks"])
                print("Total:", student["total"])
                print("Average:", round(student["average"], 2))
                print("Percentage:", round(student["percentage"], 2), "%")
                print("Grade:", student["grade"])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("❌ Invalid choice.")