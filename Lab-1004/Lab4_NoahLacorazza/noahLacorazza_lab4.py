# Part one
# 1)
user_int = int(input("Enter an int: "))

if user_int > 0:
    print("The number is positive")

if user_int == 0:
    print("The number is 0")
elif user_int % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 2)
TAX_EXEMPT_AGE = 16
EARNING_TEEN_AGE = 25
EARNING_TEEN_LOWER_INCOME = 20000
WORKING_ADULT_LOWER_INCOME = 50000

user_age = int(input("Enter your age: "))
user_income = int(input("Enter your annual salary: "))

if user_age <= TAX_EXEMPT_AGE:
    print("Tax Bracket: 0%")
elif user_age <= EARNING_TEEN_AGE:
    if user_income <= EARNING_TEEN_LOWER_INCOME:
        print("Tax Bracket: 10%")
    else:
        print("Tax Bracket: 15%")
else:
    if user_income <= WORKING_ADULT_LOWER_INCOME:
        print("Tax Bracket: 20%")
    else:
        print("Tax Bracket: 25%")

# Part two
# 3)
i = 5

while i > 0:
    print(i)
    i -= 1

# 4)
i = 1

while i <= 3:
    k = 1
    while k <= 3:
        print(k * i, end=" ")
        k += 1
    print("\n")

    i += 1