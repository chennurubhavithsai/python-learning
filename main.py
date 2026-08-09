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
        print("No foods available.")
        return

    print("\n===== FOOD DATABASE =====")

    for food in foods:

        print("\nFood:", food["name"])
        print("Protein:", food["protein"], "g")
        print("Carbohydrates:", food["carbs"], "g")
        print("Fat:", food["fat"], "g")
        print("Calories:", food["calories"], "kcal")


def search_food():

    search = input("Enter food name to search: ").lower()

    found = False

    for food in foods:

        if food["name"].lower() == search:

            print("\n✅ Food Found")
            print("Food:", food["name"])
            print("Protein:", food["protein"], "g")
            print("Carbohydrates:", food["carbs"], "g")
            print("Fat:", food["fat"], "g")
            print("Calories:", food["calories"], "kcal")

            found = True
            break

    if not found:
        print("❌ Food not found.")


while True:

    print("\n===== FOOD NUTRITION DATABASE =====")
    print("1. Add Food")
    print("2. View Foods")
    print("3. Search Food")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_food()

    elif choice == "2":
        view_foods()

    elif choice == "3":
        search_food()

    elif choice == "4":
        print("🥗 Thank you for using Nutrition Database!")
        break

    else:
        print("❌ Invalid choice.")