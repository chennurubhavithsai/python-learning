employees = []

while True:

    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

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

            for i, employee in enumerate(employees, start=1):

                print(f"\nEmployee {i}")
                print("ID         :", employee["id"])
                print("Name       :", employee["name"])
                print("Department :", employee["department"])
                print(f"Salary     : ₹{employee['salary']:.2f}")

    elif choice == "3":

        print("Thank you for using Employee Management System!")
        break

    else:

        print("❌ Invalid choice.")