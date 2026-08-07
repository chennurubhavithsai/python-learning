patients = []

while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        age = int(input("Enter Age: "))
        disease = input("Enter Disease: ")
        doctor = input("Enter Doctor Name: ")

        patients.append({
            "id": patient_id,
            "name": name,
            "age": age,
            "disease": disease,
            "doctor": doctor
        })

        print("✅ Patient added successfully!")

    elif choice == "2":

        if len(patients) == 0:
            print("No patient records found.")

        else:
            print("\n===== PATIENT LIST =====")

            for patient in patients:

                print("\nPatient ID :", patient["id"])
                print("Name       :", patient["name"])
                print("Age        :", patient["age"])
                print("Disease    :", patient["disease"])
                print("Doctor     :", patient["doctor"])

    elif choice == "3":

        print("🏥 Thank you for using Hospital Management System!")
        break

    else:

        print("❌ Invalid choice.")