import json

foods = []


# -------------------------------
# Safe number input
# -------------------------------

def get_number(message):

    while True:

        try:
            value = float(input(message))

            if value < 0:
                print("❌ Value cannot be negative.")
                continue

            return value

        except ValueError:
            print("❌ Please enter a valid number.")


# -------------------------------
# Calculate calories
# -------------------------------

def calculate_calories(protein, carbs, fat):

    return (protein * 4) + (carbs * 4) + (fat * 9)


# -------------------------------
# Add food
# -------------------------------

def add_food():

    name = input("Enter food name: ").strip()

    if name == "":
        print("❌ Food name cannot be empty.")
        return

    protein = get_number("Enter protein (g): ")
    carbs = get_number("Enter carbohydrates (g): ")
    fat = get_number("Enter fat (g): ")

    calories = calculate_calories(
        protein,
        carbs,
        fat
    )

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
# View foods
# -------------------------------

def view_foods():

    if len(foods) == 0:
        print("No foods available.")
        return

    print("\n===== FOOD DATABASE =====")

    for food in foods:

        print("\nFood:", food["name"])
        print("Protein:", food["protein"], "g")
        print("Carbs:", food["carbs"], "g")
        print("Fat:", food["fat"], "g")
        print("Calories:", f"{food['calories']:.2f}", "kcal")


# -------------------------------
# Search food
# -------------------------------

def search_food():

    name = input("Enter food name: ").strip().lower()

    found = False

    for food in foods:

        if food["name"].lower() == name:

            print("\n✅ FOOD FOUND")
            print("Food:", food["name"])
            print("Protein:", food["protein"], "g")
            print("Carbs:", food["carbs"], "g")
            print("Fat:", food["fat"], "g")
            print("Calories:", f"{food['calories']:.2f}", "kcal")

            found = True
            break

    if not found:
        print("❌ Food not found.")


# -------------------------------
# Food quality analysis
# -------------------------------

def analyze_food():

    name = input("Enter food name to analyze: ").strip().lower()

    for food in foods:

        if food["name"].lower() == name:

            print("\n===== FOOD ANALYSIS =====")
            print("Food:", food["name"])

            if food["protein"] >= 10:
                print("💪 Protein: High")
            else:
                print("Protein: Moderate/Low")

            if food["carbs"] >= 50:
                print("🍞 Carbohydrates: High")
            else:
                print("Carbohydrates: Moderate/Low")

            if food["fat"] >= 20:
                print("Fat: High")
            else:
                print("Fat: Moderate/Low")

            print(
                f"Estimated Calories: "
                f"{food['calories']:.2f} kcal"
            )

            return

    print("❌ Food not found.")


# -------------------------------
# Delete food
# -------------------------------

def delete_food():

    name = input("Enter food name to delete: ").strip().lower()

    for food in foods:

        if food["name"].lower() == name:

            foods.remove(food)

            print("✅ Food deleted successfully!")
            return

    print("❌ Food not found.")


# -------------------------------
# Save foods
# -------------------------------

def save_foods():

    try:

        with open("food_quality.json", "w") as file:

            json.dump(
                foods,
                file,
                indent=4
            )

        print("💾 Food data saved successfully!")

    except OSError:

        print("❌ Could not save the file.")


# -------------------------------
# Load foods
# -------------------------------

def load_foods():

    try:

        with open("food_quality.json", "r") as file:

            data = json.load(file)

            if isinstance(data, list):
                foods.extend(data)

            print("📂 Food data loaded successfully!")

    except FileNotFoundError:

        print("ℹ️ No previous food database found.")

    except json.JSONDecodeError:

        print("❌ The JSON file contains invalid data.")


# -------------------------------
# Load existing data
# -------------------------------

load_foods()


# -------------------------------
# Main menu
# -------------------------------

while True:

    print("\n===== FOOD QUALITY CHECKER =====")
    print("1. Add Food")
    print("2. View Foods")
    print("3. Search Food")
    print("4. Analyze Food")
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

        analyze_food()

    elif choice == "5":

        delete_food()

    elif choice == "6":

        save_foods()

    elif choice == "7":

        save_foods()

        print("🧪 Thank you for using Food Quality Checker!")
        break

    else:

        print("❌ Invalid choice.")