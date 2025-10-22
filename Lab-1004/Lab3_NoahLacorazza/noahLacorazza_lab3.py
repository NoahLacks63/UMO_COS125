# Step 1
age = int(input("Enter your age: "))
if age >= 21:
    print("You can buy alcohol.")

# Step 2
age = int(input("Enter your age: "))

if age >= 21:
    print("You can buy alcohol.")
else:
    print("You cannot buy alcohol.")

# Step 3
grade = int(input("Enter your grade: "))

if grade > 90:
    print("You got an A.")
elif grade >= 80:
    print("You got a B.")
elif grade >= 70:
    print("You got a C.")
else:
    print("You failed.")

# Step 4
YES = "yes"

age = int(input("Enter your age: "))

has_license = input("Do you have a license (yes or no): ") == YES
if age >= 16:
    if has_license:
        print("You can drive.")
    else:
        print("You cannot drive without a license.")
else:
    print("You are too young to drive.")

## CHALLENGES ##
# Challenge 1

num = int(input("Enter an integer: "))

if num == 0:
    print("Your number was 0")
else:
    if num % 2 == 0:
        print(f"Your number was {num}. {num} is even")
    else:
        print(f"Your number was {num}. {num} is odd")

# Challenge 2

RED = "red"
YELLOW = "yellow"
GREEN = "green"

YES = "yes"
NO = "no"

color = input("Enter the color of the traffic light (red, yellow, green): ")

if color == RED:
    if input("Is right on red allowed? (yes or no): ") == YES:
        if input("Is there oncoming traffic? (yes or no): ") == NO:
            print("Proceed with caution after stopping")
        else: 
            print("Stop")
    else: 
        print("Stop")
elif color == YELLOW:
    print("Caution")
elif color == GREEN:
    print("Go")

