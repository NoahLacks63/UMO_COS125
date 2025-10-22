# PROBLEM 1
print("Welcome to the Rectangle Area Calculator!")
print(type("Welcome"))

# What data type does the output indicate "Welcome" is?
# str

# What data type does print(type(42)) indicate 42 is?
# int

# What would be the data type if 42 was wrapped in quotes?
# str


# PROBLEM 2
length = input("Enter the length of the rectangle: ")
print(type(length))

length = float(length)
print(type(length))

# A more direct method:
width = float(input("Enter the width of the rectangle: "))
print(type(width))


# PROBLEM 3

fav_food = "pizza"
print("My favorite food is: ", fav_food)


# PROBLEM 4

age = input("Enter your age: ")
print("I am ", age, " year(s) old")


# PROBLEM 5

num_a = float(input("Enter first number: ")) 
num_b = float(input("Enter second number: "))
ab_sum = num_a + num_b

print(num_a)
print(num_b)
print(ab_sum)


# PROBLEM 6

length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

perimeter = (length + width) * 2
diagonal = (length**2 + width**2)**0.5

print(length)
print(width)
print(perimeter)
print(diagonal)


# PROBLEM 7

# What would "5" + "5" result in?
# 55

# What about "5" + 5?
# TypeError


# PROBLEM 8

print(1/4)
print(1//4)
print(int(1/4))
print(float(1/4))
print(1//4.0)
print(4/2.5)
print(-1//2)
print(2**2)
print(2*2)
print((2*2)**2)
print(8%3)
print(8%2)
print(((2**8)+8)/12)
print((2**8) + 8/12)
print(100+10*(6-2))
print(100+10*6-2)