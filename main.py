tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Save Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({
            "task": task,
            "completed": False
        })
        print("✅ Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== YOUR TASKS =====")
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. {task['task']} {status}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                status = "✅" if task["completed"] else "❌"
                print(f"{i}. {task['task']} {status}")

            task_number = int(input("Enter task number to complete: "))

            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("✅ Task marked as completed!")
            else:
                print("❌ Invalid task number.")

    elif choice == "4":
        with open("tasks.txt", "w") as file:
            for task in tasks:
                status = "Completed" if task["completed"] else "Pending"
                file.write(f"{task['task']} - {status}\n")

        print("✅ Tasks saved successfully!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("❌ Invalid choice!")