products = []

# Load products from file
try:
    with open("inventory.txt", "r") as file:
        for line in file:
            data = line.strip().split(",")

            if len(data) == 3:
                products.append({
                    "name": data[0],
                    "quantity": int(data[1]),
                    "price": float(data[2])
                })

except FileNotFoundError:
    pass


while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("6. Calculate Inventory Value")
    print("7. Save Inventory")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: ₹"))

        products.append({
            "name": name,
            "quantity": quantity,
            "price": price
        })

        print("✅ Product added successfully!")

    elif choice == "2":

        if len(products) == 0:
            print("No products available.")

        else:

            print("\n===== PRODUCT LIST =====")

            for i, product in enumerate(products, start=1):

                value = product["quantity"] * product["price"]

                print(f"\nProduct {i}")
                print("Name     :", product["name"])
                print("Quantity :", product["quantity"])
                print(f"Price    : ₹{product['price']:.2f}")
                print(f"Value    : ₹{value:.2f}")

    elif choice == "3":

        search = input("Enter product name: ").lower()

        found = False

        for product in products:

            if product["name"].lower() == search:

                value = product["quantity"] * product["price"]

                print("\n✅ Product Found")
                print("Name     :", product["name"])
                print("Quantity :", product["quantity"])
                print(f"Price    : ₹{product['price']:.2f}")
                print(f"Value    : ₹{value:.2f}")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    elif choice == "4":

        update = input("Enter product name to update: ").lower()

        found = False

        for product in products:

            if product["name"].lower() == update:

                product["quantity"] = int(input("Enter new quantity: "))
                product["price"] = float(input("Enter new price: ₹"))

                print("✅ Product updated successfully!")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    elif choice == "5":

        delete = input("Enter product name to delete: ").lower()

        found = False

        for product in products:

            if product["name"].lower() == delete:

                products.remove(product)

                print("✅ Product deleted successfully!")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    elif choice == "6":

        total_value = 0

        for product in products:
            total_value += product["quantity"] * product["price"]

        print(f"\n💰 Total Inventory Value: ₹{total_value:.2f}")

    elif choice == "7":

        with open("inventory.txt", "w") as file:

            for product in products:

                file.write(
                    f"{product['name']},{product['quantity']},{product['price']}\n"
                )

        print("✅ Inventory saved successfully!")

    elif choice == "8":

        print("Thank you for using Inventory Management System!")
        break

    else:

        print("❌ Invalid choice.")