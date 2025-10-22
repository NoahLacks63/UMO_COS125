fruit_rainbow = {
    "Banana": "Yellow",
    "Strawberry": "Red",
    "Pineapple": "Yellow",
    "Cantaloupe": "Orange",
    "Watermelon": "Red"
}

print(fruit_rainbow)
print(fruit_rainbow.keys())

print(fruit_rainbow[input("What fruit would you like to know the color of?: ").capitalize()])

key = input("Enter a fruit: ").capitalize()
fruit_rainbow[key] = input("Enter its color: ")
print(fruit_rainbow)