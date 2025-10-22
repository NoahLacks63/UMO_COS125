# File: noahLacorazza_classCredits.py
# Author: Noah Lacorazza
# Date: 9/8/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# Calculates the cost of credits and displays info about the user and their credits
# Collaboration:
# N/A

CREDIT_COST = 350.50

name = input("Enter your name: ")
num_credits = input("Enter number of credits: ")

num_credits = int(num_credits)

print("Name: ", name)
print("Registered credits", num_credits)
print("Cost per credit: ", CREDIT_COST)
print("Total Cost: ", num_credits * CREDIT_COST)