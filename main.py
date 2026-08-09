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

        print("No foods available.")
        return

    print("\n===== FOOD DATABASE =====")

    for food in foods:

        print("\nFood:", food["name"])
        print("Protein:", food["protein"], "g")
        print("Carbohydrates:", food["carbs"], "g")
        print("Fat:", food["fat"], "g")
        print("Calories:", food["calories"], "kcal")


# -------------------------------
# Search Food
# -------------------------------

def search_food():

    search = input("Enter food name: ").lower()

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


# -------------------------------
# Save Foods
# -------------------------------

def save_foods():

    with open("foods.txt", "w") as file:

        for food in foods:

            file.write(
                f"{food['name']},"
                f"{food['protein']},"
                f"{food['carbs']},"
                f"{food['fat']},"
                f"{food['calories']}\n"
            )

    print("💾 Foods saved successfully!")


# -------------------------------
# Load Foods
# -------------------------------

def load_foods():

    try:

        with open("foods.txt", "r") as file:

            for line in file:

                data = line.strip().split(",")

                if len(data) == 5:

                    foods.append({
                        "name": data[0],
                        "protein": float(data[1]),
                        "carbs": float(data[2]),
                        "fat": float(data[3]),
                        "calories": float(data[4])
                    })

    except FileNotFoundError:

        pass


# -------------------------------
# Nutrition Summary
# -------------------------------

def nutrition_summary():

    if len(foods) == 0:

        print("No foods available.")
        return

    total_calories = sum(
        food["calories"]
        for food in foods
    )

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

    print("\n===== NUTRITION SUMMARY =====")

    print("Total Foods:", len(foods))
    print(f"Total Calories: {total_calories:.2f} kcal")
    print(f"Total Protein: {total_protein:.2f} g")
    print(f"Total Carbohydrates: {total_carbs:.2f} g")
    print(f"Total Fat: {total_fat:.2f} g")


# -------------------------------
# Load data when program starts
# -------------------------------

load_foods()


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n===== FOOD NUTRITION DATABASE =====")
    print("1. Add Food")
    print("2. View Foods")
    print("3. Search Food")
    print("4. Nutrition Summary")
    print("5. Save Foods")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_food()

    elif choice == "2":

        view_foods()

    elif choice == "3":

        search_food()

    elif choice == "4":

        nutrition_summary()

    elif choice == "5":

        save_foods()

    elif choice == "6":

        save_foods()

        print("🥗 Thank you for using Food Nutrition Database!")
        break

    else:

        print("❌ Invalid choice.")