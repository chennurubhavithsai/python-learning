bookings = []

# Load bookings from file
try:
    with open("hotel_bookings.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 6:
                bookings.append({
                    "id": data[0],
                    "customer": data[1],
                    "room": data[2],
                    "nights": int(data[3]),
                    "price": float(data[4]),
                    "total": float(data[5])
                })

except FileNotFoundError:
    pass


while True:

    print("\n===== HOTEL RESERVATION SYSTEM =====")
    print("1. Book Room")
    print("2. View Bookings")
    print("3. Search Booking")
    print("4. Update Reservation")
    print("5. Cancel Reservation")
    print("6. Revenue Statistics")
    print("7. Save Bookings")
    print("8. Exit")

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

        delete = input("Enter Booking ID to cancel: ")

        found = False

        for booking in bookings:

            if booking["id"] == delete:

                bookings.remove(booking)

                print("✅ Booking cancelled successfully!")

                found = True
                break

        if not found:
            print("❌ Booking not found.")

    elif choice == "6":

        if len(bookings) == 0:
            print("No bookings available.")

        else:

            total_revenue = sum(b["total"] for b in bookings)
            total_bookings = len(bookings)
            highest_booking = max(bookings, key=lambda b: b["total"])

            print("\n===== REVENUE STATISTICS =====")
            print(f"Total Revenue : ₹{total_revenue:.2f}")
            print(f"Total Bookings: {total_bookings}")

            print("\n⭐ Highest Value Booking")
            print("Booking ID :", highest_booking["id"])
            print("Customer   :", highest_booking["customer"])
            print("Room No.   :", highest_booking["room"])
            print(f"Bill Amount: ₹{highest_booking['total']:.2f}")

    elif choice == "7":

        with open("hotel_bookings.txt", "w") as file:

            for booking in bookings:

                file.write(
                    f"{booking['id']},{booking['customer']},{booking['room']},{booking['nights']},{booking['price']},{booking['total']}\n"
                )

        print("✅ Bookings saved successfully!")

    elif choice == "8":

        print("Thank you for using Hotel Reservation System!")
        break

    else:

        print("❌ Invalid choice.")