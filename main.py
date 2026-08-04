employees = []

# Load employee data
try:
    with open("employees.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                employees.append({
                    "id": data[0],
                    "name": data[1],
                    "department": data[2],
                    "salary": float(data[3])
                })

except FileNotFoundError:
    pass


while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Salary Statistics")
    print("7. Save Employees")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        salary = float(input("Enter Salary: ₹"))

        employees.append({
            "id": emp_id,
            "name": name,
            "department": department,
            "salary": salary
        })

        print("✅ Employee added successfully!")

    elif choice == "2":

        if len(employees) == 0:
            print("No employee records found.")

        else:
            print("\n===== EMPLOYEE LIST =====")

            for employee in employees:

                print("\nID         :", employee["id"])
                print("Name       :", employee["name"])
                print("Department :", employee["department"])
                print(f"Salary     : ₹{employee['salary']:.2f}")

    elif choice == "3":

        search = input("Enter Employee ID: ")

        found = False

        for employee in employees:

            if employee["id"] == search:

                print("\n✅ Employee Found")
                print("ID         :", employee["id"])
                print("Name       :", employee["name"])
                print("Department :", employee["department"])
                print(f"Salary     : ₹{employee['salary']:.2f}")

                found = True
                break

        if not found:
            print("❌ Employee not found.")

    elif choice == "4":

        update = input("Enter Employee ID to update: ")

        found = False

        for employee in employees:

            if employee["id"] == update:

                employee["name"] = input("Enter New Name: ")
                employee["department"] = input("Enter New Department: ")
                employee["salary"] = float(input("Enter New Salary: ₹"))

                print("✅ Employee updated successfully!")

                found = True
                break

        if not found:
            print("❌ Employee not found.")

    elif choice == "5":

        delete = input("Enter Employee ID to delete: ")

        found = False

        for employee in employees:

            if employee["id"] == delete:

                employees.remove(employee)

                print("✅ Employee deleted successfully!")

                found = True
                break

        if not found:
            print("❌ Employee not found.")

    elif choice == "6":

        if len(employees) == 0:
            print("No employee records found.")

        else:

            total_salary = sum(emp["salary"] for emp in employees)
            average_salary = total_salary / len(employees)
            highest_paid = max(employees, key=lambda emp: emp["salary"])

            print("\n===== SALARY STATISTICS =====")
            print(f"Total Salary   : ₹{total_salary:.2f}")
            print(f"Average Salary : ₹{average_salary:.2f}")
            print("\nHighest Paid Employee")
            print("ID         :", highest_paid["id"])
            print("Name       :", highest_paid["name"])
            print("Department :", highest_paid["department"])
            print(f"Salary     : ₹{highest_paid['salary']:.2f}")

    elif choice == "7":

        with open("employees.txt", "w") as file:

            for employee in employees:

                file.write(
                    f"{employee['id']},{employee['name']},{employee['department']},{employee['salary']}\n"
                )

        print("✅ Employee records saved successfully!")

    elif choice == "8":

        print("Thank you for using Employee Management System!")
        break

    else:

        print("❌ Invalid choice.")