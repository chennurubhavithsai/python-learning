cart = []

while True:

    print("\n===== ONLINE SHOPPING SYSTEM =====")
    print("1. Add Product to Cart")
    print("2. View Cart")
    print("3. Exit")

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

        print("✅ Product added to cart successfully!")

    elif choice == "2":

        if len(cart) == 0:
            print("🛒 Your cart is empty.")

        else:

            print("\n===== SHOPPING CART =====")

            grand_total = 0

            for item in cart:

                print("\nProduct :", item["product"])
                print("Quantity:", item["quantity"])
                print(f"Price   : ₹{item['price']:.2f}")
                print(f"Total   : ₹{item['total']:.2f}")

                grand_total += item["total"]

            print(f"\n🧾 Cart Total: ₹{grand_total:.2f}")

    elif choice == "3":

        print("🛍️ Thank you for shopping with us!")
        break

    else:

        print("❌ Invalid choice.")