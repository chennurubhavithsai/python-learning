bookings = []

while True:

    print("\n===== HOTEL RESERVATION SYSTEM =====")
    print("1. Book Room")
    print("2. View Bookings")
    print("3. Search Booking")
    print("4. Update Reservation")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        booking_id = input("Enter Booking ID: ")
        customer = input("Enter Customer Name: ")
        room = input("Enter Room Number: ")
        nights = int(input("Enter Number of Nights: "))
        price = float(input("Enter Price Per Night (₹): "))

        total = nights * price

        bookings.append({
            "id": booking_id,
            "customer": customer,
            "room": room,
            "nights": nights,
            "price": price,
            "total": total
        })

        print("✅ Room booked successfully!")

    elif choice == "2":

        if len(bookings) == 0:
            print("No bookings found.")

        else:

            print("\n===== BOOKING LIST =====")

            for booking in bookings:

                print("\nBooking ID :", booking["id"])
                print("Customer   :", booking["customer"])
                print("Room No.   :", booking["room"])
                print("Nights     :", booking["nights"])
                print(f"Price/Night: ₹{booking['price']:.2f}")
                print(f"Total Bill : ₹{booking['total']:.2f}")

    elif choice == "3":

        search = input("Enter Booking ID: ")

        found = False

        for booking in bookings:

            if booking["id"] == search:

                print("\n✅ Booking Found")
                print("Booking ID :", booking["id"])
                print("Customer   :", booking["customer"])
                print("Room No.   :", booking["room"])
                print("Nights     :", booking["nights"])
                print(f"Price/Night: ₹{booking['price']:.2f}")
                print(f"Total Bill : ₹{booking['total']:.2f}")

                found = True
                break

        if not found:
            print("❌ Booking not found.")

    elif choice == "4":

        update = input("Enter Booking ID to update: ")

        found = False

        for booking in bookings:

            if booking["id"] == update:

                booking["customer"] = input("Enter New Customer Name: ")
                booking["room"] = input("Enter New Room Number: ")
                booking["nights"] = int(input("Enter New Number of Nights: "))
                booking["price"] = float(input("Enter New Price Per Night (₹): "))

                booking["total"] = booking["nights"] * booking["price"]

                print("✅ Reservation updated successfully!")

                found = True
                break

        if not found:
            print("❌ Booking not found.")

    elif choice == "5":

        print("Thank you for using Hotel Reservation System!")
        break

    else:

        print("❌ Invalid choice.")