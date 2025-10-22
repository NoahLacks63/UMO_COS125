# File: noahLacorazza_internet.py
# Author: Noah Lacorazza
# Date: 9/15/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# Selects an internet package based on minimum requirements inputted by the user
# Collaboration:
# N/A

# I hate this without being able to use complex data types :(
STANDARD_PACKAGE = "Standard Package"
STANDARD_SPEED = 150
STANDARD_DATA = 1000
STANDARD_PRICE = 65

PREMIUM_PACKAGE = "Premium Package"
PREMIUM_SPEED = 500
PREMIUM_DATA = "Unlimited"
PREMIUM_PRICE = 90

# basic package by default
selected_package = "Basic Package"
selected_speed = 50
selected_data = 500
selected_price = 40

name = input("Enter your name: ")
speed_mbps = int(input("Enter download speed in Mbps: "))
monthly_data = int(input("Enter your average monthly data usage in GB: "))
monthly_budget = float(input("Enter your monthly budget in dollars: "))

if monthly_data >= STANDARD_DATA or speed_mbps >= STANDARD_SPEED:
    selected_package = PREMIUM_PACKAGE
    selected_speed = PREMIUM_SPEED
    selected_data = PREMIUM_DATA
    selected_price = PREMIUM_PRICE
elif monthly_data <= selected_data or speed_mbps <= selected_speed:
    selected_package = STANDARD_PACKAGE
    selected_speed = STANDARD_SPEED
    selected_data = STANDARD_DATA
    selected_price = STANDARD_PRICE

print(f"""Thank you, {name}. 
    Based on your needs, we recommend the {selected_package} with {selected_speed} Mbps speed and {selected_data} GB data. 
    It costs ${selected_price} per month, which is {"not " if selected_price > monthly_budget else ""}within your budget of ${monthly_budget:.2f}.""")


### No restrictions ###
# I did this for fun, no grading below this point lol

PACKAGES = [
    {
        "name": "Basic", 
        "speed": 50,
        "data": 500,
        "cost": 40
    },
    {
        "name": "Standard",
        "speed": 150,
        "data": 1000,
        "price": 65
    },
    {
        "name": "Premium",
        "speed": 500,
        "data": "Unlimited",
        "price": 90
    }
]

user_name = input("Enter your name: ")
user_speed = int(input("Enter required speed in MBPS: "))
user_data = int(input("Enter required data in GB: "))
user_budget = float(input("Enter your monthly internet budget: "))

selected_package = 0

if user_speed >= PACKAGES[1]["speed"] or user_data >= PACKAGES[1]["data"]:
    selected_package = 2
elif user_speed >= PACKAGES[0]["speed"] or user_data >= PACKAGES[0]["data"]:
    selected_package = 1

print(f"""Thank you, {name}. 
    Based on your needs, we recommend the {PACKAGES[selected_package]["name"]} Package with {PACKAGES[selected_package]["speed"]} Mbps speed and {PACKAGES[selected_package]["data"]} GB data. 
    It costs ${PACKAGES[selected_package]["price"]} per month, which is {"not " if PACKAGES[selected_package]["price"] > user_budget else ""}within your budget of ${user_budget:.2f}.""")
