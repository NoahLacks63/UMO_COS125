total = float(input("Enter total: "))
tip_percentage = float(input("Enter tip %: "))

def tip_calculator(total, tip_percentage):
    return total * (tip_percentage / 100 + 1)

tip_total = tip_calculator(total, tip_percentage)

print(f"Your total after tipping is: {tip_total}")