# File: noahLacorazza_Inventory.py
# Author: Noah Lacorazza
# Date: 10/5/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# 
# Collaboration:
# N/A

num_warehouses = int(input("Enter number of warehouses: "))

warehouses = [None] * num_warehouses


for warehouse_num in range(num_warehouses):
    warehouses[warehouse_num] = [input("Enter warehouse name: ")]

    for category in range(int(input("Enter num of categories for this warehouse: "))):
        warehouses[warehouse_num].append([input("Enter category name: ")])

        for item in range(int(input("Enter num of items in this category: "))):
            item_name = input("Enter name of item: ")

            warehouses[warehouse_num][category+1].append(input("Enter num of initial stock: "))
            warehouses[warehouse_num][category+1].append(item_name)

print("--The Total Inventory--")

for warehouse in warehouses:
    print(f"{warehouse[0]}: ")

    for category in warehouse[1:]:
        print(f"\t{category[0]}: {', '.join(category[1:])}")

user_search = input("Enter item name: ")

# Index for which warehouse we are searching through
warehouse = 0
# Index for which category we are searching through
category = 1
# Index for which item we are looking at (only even numbers because odds are their stock #)
item = 2
# The item we are comparing to
comparator = None

while warehouse < len(warehouses) and comparator != user_search:
    while category < len(warehouses[warehouse]) and comparator != user_search:
        item = 0
        while item < len(warehouses[warehouse][category]) and comparator != user_search:
            comparator = warehouses[warehouse][category][item]

            item += 2

        category += 1
        
    warehouse += 1

ADD_TRANSACTION = "add"
REMOVE_TRANSACTION = "remove"

if comparator == user_search:
    warehouse -= 1
    category -= 1
    item -= 3
    print(item)
    print(f"Item located in {warehouses[warehouse][0]}, {warehouses[warehouse][category][0]}, and its initial stock is {warehouses[warehouse][category][item]}")
    
    transaction_type = input("Enter transaction type ('add' or 'remove'): ")
    transaction_amount = int(input("Enter the transaction amount: "))

    if transaction_type == ADD_TRANSACTION:
        if int(warehouses[warehouse][category][item]) + transaction_amount < 0:
            print("Transaction failed :(")
        else:
            warehouses[warehouse][category][item] = str(int(warehouses[warehouse][category][item]) + transaction_amount)
    elif transaction_type == REMOVE_TRANSACTION:
        if int(warehouses[warehouse][category][item]) - transaction_amount <= 0:
            print("Transaction failed :(")
        else:
            warehouses[warehouse][category][item] = str(int(warehouses[warehouse][category][item]) - transaction_amount)
else:
    print("Item not found :(")

for warehouse in warehouses:
    print(f"{warehouse[0]}: ")

    for category in warehouse[1:]:
        print(f"\t{category[0]}: ", end="")

        for item in range(1, len(category)):
            if item % 2 == 1:
                print(category[item], end=" ")
            else:
                print(category[item], end=", ")

        print("")