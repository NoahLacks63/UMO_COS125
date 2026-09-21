# Comment header

import random


name = input("Enter your name: ")
balance = int(input("Enter starting balance (int): "))
custom_hall = input("Enter custom venue: ")

dining_halls = ["union", "hilltop"]
dining_halls.append(custom_hall)

daily_expenses = []

for i in range(len(dining_halls)):
    print(f"Venue {i}: {dining_halls[i]}")

while balance > 5.00:
    expense = random.randrange(8, 16)
    daily_expenses.append(expense)
    balance.append(expense)

print

total_expenses = sum(daily_expenses)
avg_expenses = total_expenses / len(daily_expenses)

