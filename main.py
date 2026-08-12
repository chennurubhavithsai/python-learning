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


print("===== FOOD QUALITY CHECKER =====")

food_name = input("Enter food name: ")

protein = get_number("Enter protein (g): ")
carbs = get_number("Enter carbohydrates (g): ")
fat = get_number("Enter fat (g): ")

print("\n===== FOOD INFORMATION =====")
print("Food:", food_name)
print("Protein:", protein, "g")
print("Carbohydrates:", carbs, "g")
print("Fat:", fat, "g")