students = []

while True:

    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Attendance Percentage")
    print("5. Update Attendance")
    print("6. Exit")

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

                print("\nStudent ID :", student["id"])
                print("Name       :", student["name"])
                print("Present    :", student["present"])
                print("Total Days :", student["total_days"])

    # Mark Attendance
    elif choice == "3":

        student_id = input("Enter Student ID: ")

        found = False

        for student in students:

            if student["id"] == student_id:

                attendance = input("Enter attendance (P/A): ").upper()

                if attendance == "P":

                    student["present"] += 1
                    student["total_days"] += 1

                    print("✅ Attendance marked PRESENT.")

                elif attendance == "A":

                    student["total_days"] += 1

                    print("❌ Attendance marked ABSENT.")

                else:

                    print("❌ Invalid attendance. Use P or A.")

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

                print("\nCurrent Attendance:")
                print("Present    :", student["present"])
                print("Total Days :", student["total_days"])

                present = int(input("Enter new Present Days: "))
                total_days = int(input("Enter new Total Days: "))

                if present < 0 or total_days < 0:
                    print("❌ Values cannot be negative.")

                elif present > total_days:
                    print("❌ Present days cannot be greater than total days.")

                else:

                    student["present"] = present
                    student["total_days"] = total_days

                    print("✅ Attendance updated successfully!")

                found = True
                break

        if not found:
            print("❌ Student not found.")

    # Exit
    elif choice == "6":

        print("Thank you for using Student Attendance System!")
        break

    else:

        print("❌ Invalid choice.")