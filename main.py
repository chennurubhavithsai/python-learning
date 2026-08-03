products = []

while True:

    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. Add Product")
    print("2. View Products")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price per item: ₹"))

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

        print("Thank you for using Inventory Management System!")
        break

    else:

        print("❌ Invalid choice.")