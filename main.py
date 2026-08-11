import json

foods = []


def calculate_calories(protein, carbs, fat):
    return (protein * 4) + (carbs * 4) + (fat * 9)


def add_food():

    name = input("Enter food name: ")
    protein = float(input("Enter protein (g): "))
    carbs = float(input("Enter carbohydrates (g): "))
    fat = float(input("Enter fat (g): "))

    calories = calculate_calories(protein, carbs, fat)

    food = {
        "name": name,
        "protein": protein,
        "carbs": carbs,
        "fat": fat,
        "calories": calories
    }

    foods.append(food)

    print("✅ Food added successfully!")


def view_foods():

    if len(foods) == 0:
        print("No foods found.")
        return

    print("\n===== FOOD DATABASE =====")

    for food in foods:

        print("\nFood:", food["name"])
        print("Protein:", food["protein"], "g")
        print("Carbs:", food["carbs"], "g")
        print("Fat:", food["fat"], "g")
        print("Calories:", food["calories"], "kcal")


def search_food():

    name = input("Enter food name to search: ").lower()

    found = False

    for food in foods:

        if food["name"].lower() == name:

            print("\n✅ FOOD FOUND")
            print("Food:", food["name"])
            print("Protein:", food["protein"], "g")
            print("Carbs:", food["carbs"], "g")
            print("Fat:", food["fat"], "g")
            print("Calories:", food["calories"], "kcal")

            found = True
            break

    if not found:
        print("❌ Food not found.")


def update_food():

    name = input("Enter food name to update: ").lower()

    found = False

    for food in foods:

        if food["name"].lower() == name:

            print("\nEnter new nutrition values:")

            food["protein"] = float(
                input("Protein (g): ")
            )

            food["carbs"] = float(
                input("Carbohydrates (g): ")
            )

            food["fat"] = float(
                input("Fat (g): ")
            )

            food["calories"] = calculate_calories(
                food["protein"],
                food["carbs"],
                food["fat"]
            )

            print("✅ Food updated successfully!")

            found = True
            break

    if not found:
        print("❌ Food not found.")


def delete_food():

    name = input("Enter food name to delete: ").lower()

    found = False

    for food in foods:

        if food["name"].lower() == name:

            foods.remove(food)

            print("✅ Food deleted successfully!")

            found = True
            break

    if not found:
        print("❌ Food not found.")


def save_foods():

    with open("foods.json", "w") as file:

        json.dump(
            foods,
            file,
            indent=4
        )

    print("💾 Database saved successfully!")


while True:

    print("\n===== FOOD PRODUCT DATABASE =====")
    print("1. Add Food")
    print("2. View Foods")
    print("3. Search Food")
    print("4. Update Food")
    print("5. Delete Food")
    print("6. Save Foods")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_food()

    elif choice == "2":
        view_foods()

    elif choice == "3":
        search_food()

    elif choice == "4":
        update_food()

    elif choice == "5":
        delete_food()

    elif choice == "6":
        save_foods()

    elif choice == "7":
        print("🥗 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")