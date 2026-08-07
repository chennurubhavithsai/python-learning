patients = []

while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Exit")

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

        search = input("Enter Patient ID: ")

        found = False

        for patient in patients:

            if patient["id"] == search:

                print("\n✅ Patient Found")
                print("Patient ID :", patient["id"])
                print("Name       :", patient["name"])
                print("Age        :", patient["age"])
                print("Disease    :", patient["disease"])
                print("Doctor     :", patient["doctor"])

                found = True
                break

        if not found:
            print("❌ Patient not found.")

    elif choice == "4":

        update = input("Enter Patient ID to update: ")

        found = False

        for patient in patients:

            if patient["id"] == update:

                patient["name"] = input("Enter New Name: ")
                patient["age"] = int(input("Enter New Age: "))
                patient["disease"] = input("Enter New Disease: ")
                patient["doctor"] = input("Enter New Doctor Name: ")

                print("✅ Patient details updated successfully!")

                found = True
                break

        if not found:
            print("❌ Patient not found.")

    elif choice == "5":

        print("🏥 Thank you for using Hospital Management System!")
        break

    else:

        print("❌ Invalid choice.")