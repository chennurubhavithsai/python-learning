cart = []

while True:

    print("\n===== ONLINE SHOPPING SYSTEM =====")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        product = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price per Item (₹): "))

        total = quantity * price

        cart.append({
            "product": product,
            "quantity": quantity,
            "price": price,
            "total": total
        })

        print("✅ Product added successfully!")

    elif choice == "2":

        if len(cart) == 0:
            print("🛒 Cart is empty.")

        else:

            grand_total = 0

            print("\n===== SHOPPING CART =====")

            for item in cart:

                print("\nProduct :", item["product"])
                print("Quantity:", item["quantity"])
                print(f"Price   : ₹{item['price']:.2f}")
                print(f"Total   : ₹{item['total']:.2f}")

                grand_total += item["total"]

            print(f"\n🧾 Grand Total: ₹{grand_total:.2f}")

    elif choice == "3":

        search = input("Enter Product Name: ").lower()

        found = False

        for item in cart:

            if item["product"].lower() == search:

                print("\n✅ Product Found")
                print("Product :", item["product"])
                print("Quantity:", item["quantity"])
                print(f"Price   : ₹{item['price']:.2f}")
                print(f"Total   : ₹{item['total']:.2f}")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    elif choice == "4":

        update = input("Enter Product Name to update: ").lower()

        found = False

        for item in cart:

            if item["product"].lower() == update:

                item["quantity"] = int(input("Enter New Quantity: "))
                item["total"] = item["quantity"] * item["price"]

                print("✅ Quantity updated successfully!")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    elif choice == "5":

        print("🛍️ Thank you for shopping with us!")
        break

    else:

        print("❌ Invalid choice.")