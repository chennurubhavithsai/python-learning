import json

foods = []


# -------------------------------
# Calculate Calories
# -------------------------------

def calculate_calories(protein, carbs, fat):
    return (protein * 4) + (carbs * 4) + (fat * 9)


# -------------------------------
# Add Food
# -------------------------------

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


# -------------------------------
# View Foods
# -------------------------------

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


# -------------------------------
# Search Food
# -------------------------------

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


# -------------------------------
# Update Food
# -------------------------------

def update_food():

    name = input("Enter food name to update: ").lower()

    found = False

    for food in foods:

        if food["name"].lower() == name:

            food["protein"] = float(
                input("New protein (g): ")
            )

            food["carbs"] = float(
                input("New carbohydrates (g): ")
            )

            food["fat"] = float(
                input("New fat (g): ")
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


# -------------------------------
# Delete Food
# -------------------------------

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


# -------------------------------
# Save Foods
# -------------------------------

def save_foods():

    with open("foods.json", "w") as file:

        json.dump(
            foods,
            file,
            indent=4
        )

    print("💾 Database saved successfully!")


# -------------------------------
# Load Foods
# -------------------------------

def load_foods():

    try:

        with open("foods.json", "r") as file:

            data = json.load(file)

            foods.extend(data)

        print("📂 Food database loaded successfully!")

    except FileNotFoundError:

        print("ℹ️ No existing database found.")

    except json.JSONDecodeError:

        print("❌ foods.json contains invalid data.")


# -------------------------------
# Nutrition Statistics
# -------------------------------

def statistics():

    if len(foods) == 0:

        print("No food data available.")
        return

    total_protein = sum(
        food["protein"]
        for food in foods
    )

    total_carbs = sum(
        food["carbs"]
        for food in foods
    )

    total_fat = sum(
        food["fat"]
        for food in foods
    )

    total_calories = sum(
        food["calories"]
        for food in foods
    )

    highest_calorie_food = max(
        foods,
        key=lambda food: food["calories"]
    )

    print("\n===== NUTRITION STATISTICS =====")

    print("Total Foods:", len(foods))
    print(f"Total Protein: {total_protein:.2f} g")
    print(f"Total Carbs: {total_carbs:.2f} g")
    print(f"Total Fat: {total_fat:.2f} g")
    print(f"Total Calories: {total_calories:.2f} kcal")

    print("\n🏆 Highest-Calorie Food")
    print("Food:", highest_calorie_food["name"])
    print(
        f"Calories: "
        f"{highest_calorie_food['calories']:.2f} kcal"
    )


# -------------------------------
# Load database
# -------------------------------

load_foods()


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n===== FOOD PRODUCT DATABASE =====")
    print("1. Add Food")
    print("2. View Foods")
    print("3. Search Food")
    print("4. Update Food")
    print("5. Delete Food")
    print("6. Nutrition Statistics")
    print("7. Save Foods")
    print("8. Exit")

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
        statistics()

    elif choice == "7":
        save_foods()

    elif choice == "8":

        save_foods()

        print("🥗 Thank you for using Food Product Database!")
        break

    else:
        print("❌ Invalid choice.")