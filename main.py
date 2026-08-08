students = []


# Load saved records
try:
    with open("attendance.txt", "r") as file:

        for line in file:

            data = line.strip().split(",")

            if len(data) == 4:

                students.append({
                    "id": data[0],
                    "name": data[1],
                    "present": int(data[2]),
                    "total_days": int(data[3])
                })

except FileNotFoundError:
    pass


while True:

    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Attendance Percentage")
    print("5. Update Attendance")
    print("6. Delete Student")
    print("7. Attendance Statistics")
    print("8. Save Records")
    print("9. Exit")

    choice = input("Enter your choice: ")


    # Add Student
    if choice == "1":

        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")

        students.append({
            "id": student_id,
            "name": name,
            "present": 0,
            "total_days": 0
        })

        print("✅ Student added successfully!")


    # View Students
    elif choice == "2":

        if len(students) == 0:

            print("No students found.")

        else:

            print("\n===== STUDENT LIST =====")

            for student in students:

                if student["total_days"] > 0:
                    percentage = (
                        student["present"]
                        / student["total_days"]
                    ) * 100
                else:
                    percentage = 0

                print("\nStudent ID :", student["id"])
                print("Name       :", student["name"])
                print("Present    :", student["present"])
                print("Total Days :", student["total_days"])
                print(f"Attendance : {percentage:.2f}%")


    # Mark Attendance
    elif choice == "3":

        student_id = input("Enter Student ID: ")

        found = False

        for student in students:

            if student["id"] == student_id:

                attendance = input(
                    "Enter attendance (P/A): "
                ).upper()

                if attendance == "P":

                    student["present"] += 1
                    student["total_days"] += 1

                    print("✅ Marked PRESENT.")

                elif attendance == "A":

                    student["total_days"] += 1

                    print("❌ Marked ABSENT.")

                else:

                    print("❌ Use only P or A.")

                found = True
                break

        if not found:
            print("❌ Student not found.")


    # Attendance Percentage
    elif choice == "4":

        student_id = input("Enter Student ID: ")

        found = False

        for student in students:

            if student["id"] == student_id:

                if student["total_days"] > 0:

                    percentage = (
                        student["present"]
                        / student["total_days"]
                    ) * 100

                    print("\n===== ATTENDANCE =====")
                    print("Student :", student["name"])
                    print("Present :", student["present"])
                    print("Total   :", student["total_days"])
                    print(f"Percentage: {percentage:.2f}%")

                else:

                    print("No attendance records yet.")

                found = True
                break

        if not found:
            print("❌ Student not found.")


    # Update Attendance
    elif choice == "5":

        student_id = input("Enter Student ID: ")

        found = False

        for student in students:

            if student["id"] == student_id:

                present = int(
                    input("Enter new Present Days: ")
                )

                total_days = int(
                    input("Enter new Total Days: ")
                )

                if present < 0 or total_days < 0:

                    print("❌ Values cannot be negative.")

                elif present > total_days:

                    print(
                        "❌ Present days cannot exceed total days."
                    )

                else:

                    student["present"] = present
                    student["total_days"] = total_days

                    print(
                        "✅ Attendance updated successfully!"
                    )

                found = True
                break

        if not found:
            print("❌ Student not found.")


    # Delete Student
    elif choice == "6":

        student_id = input(
            "Enter Student ID to delete: "
        )

        found = False

        for student in students:

            if student["id"] == student_id:

                students.remove(student)

                print("✅ Student deleted successfully!")

                found = True
                break

        if not found:
            print("❌ Student not found.")


    # Statistics
    elif choice == "7":

        if len(students) == 0:

            print("No student records found.")

        else:

            total_present = sum(
                student["present"]
                for student in students
            )

            total_days = sum(
                student["total_days"]
                for student in students
            )

            if total_days > 0:

                overall_percentage = (
                    total_present / total_days
                ) * 100

            else:

                overall_percentage = 0

            highest_student = None

            highest_percentage = -1

            for student in students:

                if student["total_days"] > 0:

                    percentage = (
                        student["present"]
                        / student["total_days"]
                    ) * 100

                    if percentage > highest_percentage:

                        highest_percentage = percentage
                        highest_student = student

            print("\n===== ATTENDANCE STATISTICS =====")
            print("Total Students:", len(students))
            print("Total Present :", total_present)
            print("Total Days    :", total_days)
            print(
                f"Overall Attendance: "
                f"{overall_percentage:.2f}%"
            )

            if highest_student is not None:

                print("\n🏆 Highest Attendance")
                print("Student :", highest_student["name"])
                print(
                    f"Percentage: "
                    f"{highest_percentage:.2f}%"
                )


    # Save Records
    elif choice == "8":

        with open("attendance.txt", "w") as file:

            for student in students:

                file.write(
                    f"{student['id']},"
                    f"{student['name']},"
                    f"{student['present']},"
                    f"{student['total_days']}\n"
                )

        print("✅ Attendance records saved successfully!")


    # Exit
    elif choice == "9":

        print(
            "🎉 Thank you for using "
            "Student Attendance System!"
        )

        break


    else:

        print("❌ Invalid choice.")