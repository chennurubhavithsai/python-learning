students = []

while True:

    print("\n===== STUDENT RESULT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Results")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Exit")

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

        print("✅ Student added successfully!")

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

        search = input("Enter student name: ").lower()

        found = False

        for student in students:

            if student["name"].lower() == search:

                print("\n✅ Student Found")
                print("Name:", student["name"])
                print("Marks:", student["marks"])
                print("Total:", student["total"])
                print("Average:", round(student["average"], 2))
                print("Percentage:", round(student["percentage"], 2), "%")
                print("Grade:", student["grade"])

                found = True
                break

        if not found:
            print("❌ Student not found.")

    elif choice == "4":

        update = input("Enter student name to update: ").lower()

        found = False

        for student in students:

            if student["name"].lower() == update:

                marks = []

                for i in range(1, 6):
                    mark = float(input(f"Enter new marks for Subject {i}: "))
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

                student["marks"] = marks
                student["total"] = total
                student["average"] = average
                student["percentage"] = percentage
                student["grade"] = grade

                print("✅ Student marks updated successfully!")

                found = True
                break

        if not found:
            print("❌ Student not found.")

    elif choice == "5":

        print("Thank you for using Student Result Management System!")
        break

    else:
        print("❌ Invalid choice.")