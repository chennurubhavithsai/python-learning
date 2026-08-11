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


def save_foods():

    with open("foods.json", "w") as file:
        json.dump(foods, file, indent=4)

    print("💾 Food database saved to foods.json!")


while True:

    print("\n===== FOOD PRODUCT DATABASE =====")
    print("1. Add Food")
    print("2. View Foods")
    print("3. Save Foods")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_food()

    elif choice == "2":
        view_foods()

    elif choice == "3":
        save_foods()

    elif choice == "4":
        print("🥗 Goodbye!")
        break

    else:
        print("❌ Invalid choice.")