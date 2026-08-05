bookings = []

while True:

    print("\n===== HOTEL RESERVATION SYSTEM =====")
    print("1. Book Room")
    print("2. View Bookings")
    print("3. Exit")

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

        print("Thank you for using Hotel Reservation System!")
        break

    else:

        print("❌ Invalid choice.")