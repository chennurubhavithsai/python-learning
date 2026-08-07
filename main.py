patients = []

# Load patient records
try:
    with open("patients.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 5:
                patients.append({
                    "id": data[0],
                    "name": data[1],
                    "age": int(data[2]),
                    "disease": data[3],
                    "doctor": data[4]
                })

except FileNotFoundError:
    pass


while True:

    print("\n===== HOSPITAL MANAGEMENT SYSTEM =====")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Patient Statistics")
    print("7. Save Records")
    print("8. Exit")

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

                print("✅ Patient updated successfully!")

                found = True
                break

        if not found:
            print("❌ Patient not found.")

    elif choice == "5":

        delete = input("Enter Patient ID to delete: ")

        found = False

        for patient in patients:

            if patient["id"] == delete:

                patients.remove(patient)

                print("✅ Patient deleted successfully!")

                found = True
                break

        if not found:
            print("❌ Patient not found.")

    elif choice == "6":

        if len(patients) == 0:
            print("No patient records found.")

        else:

            print("\n===== PATIENT STATISTICS =====")
            print("Total Patients:", len(patients))

            doctor_count = {}

            for patient in patients:

                doctor = patient["doctor"]

                if doctor in doctor_count:
                    doctor_count[doctor] += 1
                else:
                    doctor_count[doctor] = 1

            print("\nPatients per Doctor:")

            for doctor, count in doctor_count.items():
                print(f"{doctor}: {count}")

    elif choice == "7":

        with open("patients.txt", "w") as file:

            for patient in patients:

                file.write(
                    f"{patient['id']},{patient['name']},{patient['age']},{patient['disease']},{patient['doctor']}\n"
                )

        print("✅ Patient records saved successfully!")

    elif choice == "8":

        print("🏥 Thank you for using Hospital Management System!")
        break

    else:

        print("❌ Invalid choice.")