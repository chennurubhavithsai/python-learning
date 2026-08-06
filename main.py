cart = []

# Load previous orders
try:
    with open("orders.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 4:
                product = data[0]
                quantity = int(data[1])
                price = float(data[2])
                total = float(data[3])

                cart.append({
                    "product": product,
                    "quantity": quantity,
                    "price": price,
                    "total": total
                })

except FileNotFoundError:
    pass


while True:

    print("\n===== ONLINE SHOPPING SYSTEM =====")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Search Product")
    print("4. Update Quantity")
    print("5. Remove Product")
    print("6. Checkout")
    print("7. Save Orders")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        product = input("Enter Product Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price (₹): "))

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

            print(f"\nGrand Total: ₹{grand_total:.2f}")

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

        update = input("Enter Product Name to Update: ").lower()

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

        delete = input("Enter Product Name to Remove: ").lower()

        found = False

        for item in cart:

            if item["product"].lower() == delete:

                cart.remove(item)

                print("✅ Product removed successfully!")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    elif choice == "6":

        if len(cart) == 0:
            print("🛒 Cart is empty.")

        else:

            grand_total = sum(item["total"] for item in cart)

            discount = 0

            if grand_total >= 5000:
                discount = grand_total * 0.10

            final_bill = grand_total - discount

            print("\n===== CHECKOUT =====")
            print(f"Total Amount : ₹{grand_total:.2f}")
            print(f"Discount     : ₹{discount:.2f}")
            print(f"Final Bill   : ₹{final_bill:.2f}")

    elif choice == "7":

        with open("orders.txt", "w") as file:

            for item in cart:

                file.write(
                    f"{item['product']},{item['quantity']},{item['price']},{item['total']}\n"
                )

        print("✅ Orders saved successfully!")

    elif choice == "8":

        print("🛍️ Thank you for shopping with us!")
        break

    else:

        print("❌ Invalid choice.")