students = []

while True:

    print("\n===== STUDENT ATTENDANCE SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Mark Attendance")
    print("4. Exit")

    choice = input("Enter your choice: ")

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
                    print("Invalid attendance. Use P or A.")

                found = True
                break

        if not found:
            print("❌ Student not found.")

    elif choice == "4":

        print("Thank you for using Student Attendance System!")
        break

    else:

        print("❌ Invalid choice.")