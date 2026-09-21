import random

### Exercise 1 ###
#   List | Tuple | Dict
# 1   X             X
# 2                 X
# 3   X      X
# 4   X
# 5   X      X      X
# 6   

### Exercise 2 ###

# 1 
# output = [50, 99, 10, 15, 20, 25]

# 2 
# output = "Key Missing"

# 3
# output = 10

### Exercise 3 ###

num = random.randint(0, 3)

options = ["Rock", "Paper", "Scissors"]

print(options[num])

### Exercise 4 ###

def odd_sum(list):
    sum = 0

    for n in list:
        if n % 2 == 1:
            sum += n
    
    return sum

### Exercise 5 ###

def course():
    course_id = "COS 125"
    return course_id

### Exercise 6 ###

def check_key(dict, str):
    if str in dict:
        print("Key found")
    else:
        print("Key not found")

### Exercise 7 ###

def calculate_total_value(list):
    total = 0

    for dict in list:
        total += dict["price"]

    return total

calculate_total_value([
    {"price" : 45},
    {"price" : 10}
])

### Exercise 8 ###

def remove_vowels(str):
    result = ""

    vowels = ["a", "e", "i", "o", "u"]

    for c in str.lower():
        if c not in vowels:
            result += c
    
print(remove_vowels(
    "This is a certified hood classic"
))

### Exercise 9 ###

def count100():
    list = []
    for n in range(0, 100):
        list.append(n)
    
    print(f"List of numbers from 0-99: {list}")

    return list

def split_even_odd(list):
    even = []
    odd = []

    for n in list:
        if n % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return [even, odd]

print(f"Even numbers list: {split_even_odd(count100())[0]}")
print(f"Odd numbers list: {split_even_odd(count100())[1]}")

### Exercise 10 ###

weapons = ["bow", "sword", "gun"]

weapon = random.choice(weapons)

damage_bounds = [random.randint(1, 101), random.randint(1, 101)]

min_damage = min(damage_bounds)
max_damage = max(damage_bounds)

n = random.randint(1, 6)

damage_types = ["fire", "water", "air"]

if n == 1:
    extra_damage_type = random.choice(damage_types)
else:
    extra_damage_type = "None"

adjectives = ["Cool", "Awesome", "Jonah's", "Brianna's"]

print(f"NAME: {random.choice(adjectives)} {weapon}")
print(f"MIN/MAX DAMAGE: {min_damage}-{max_damage}")

if extra_damage_type != "None":
    extra_dmg = random.randint(1, 101)

    print(f"ADDITIONAL DAMAGE TYPE/AMT: {extra_damage_type} + {extra_dmg}")
else:
    print(f"ADDITIONAL DAMAGE: None")