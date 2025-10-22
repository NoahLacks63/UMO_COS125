# \t = tab
# \n = new line

num1 = int(input("Input num1: "))
num2 = int(input("Input num2: "))

if num1 % num2 == 0:
    print("evenly divisible")
elif num1 // num2 >= 1:
    print("Its got a 1")
else:
    print("not evenly divisible")

