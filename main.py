
def calculate_calories(protein, carbs, fat):
    calories = (protein * 4) + (carbs * 4) + (fat * 9)
    return calories


def calculate_protein(protein):
    return protein


def calculate_carbs(carbs):
    return carbs


def calculate_fat(fat):
    return fat


print("===== FOOD NUTRITION CALCULATOR =====")

food = input("Enter food name: ")

protein = float(input("Enter protein (g): "))
carbs = float(input("Enter carbohydrates (g): "))
fat = float(input("Enter fat (g): "))

calories = calculate_calories(protein, carbs, fat)

print("\n===== NUTRITION INFORMATION =====")
print("Food:", food)
print("Protein:", protein, "g")
print("Carbohydrates:", carbs, "g")
print("Fat:", fat, "g")
print("Calories:", calories, "kcal")