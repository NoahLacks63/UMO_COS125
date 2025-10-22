def addNums(num1, num2):
    total = num1 + num2
    return total

result = addNums(8, 9)
print(result)

firstNum = int(input("Enter a number: "))
secondNum = int(input("Enter another number: "))
result = addNums(firstNum, secondNum)
print(result)
# the function adds them together
# because they're both ints
# the return returns the sum. the result variable saves the sum

def createList(length):
    numList = []

    for i in range(length):
        numList.append(i)

    return numList

length = int(input("How long do you want this list?: "))
newList = createList(length)
print(newList)
# list (int)
def createList():
    length = int(input("How long do you want this list?: "))

    numList = []

    for i in range(length):
        numList.append(i)

    return numList

print(newList)
# technically yes. as long as its not used in a non-list way

import math, random
def calcCircleArea(radius):
    area = math.pi * (radius ** 2)
    return area

ressult = calcCircleArea(5)
print(result)

result = calcCircleArea(random.randint(1, 10))
print(result)
# it imports math and random.
# it would try to import something by the name "math random"
# a random number 1-10

country_capitals = {
    "Germany": "Berlin",
    "Canada": "Ottawa",
    "England": "London",
    "Korea": "Seoul"
}

print(country_capitals)
print(country_capitals["Canada"])
# It will ask for the value of key "Canada"
# "England": "London"
# It will print the country_capitals dictionary then the value of key "Canada"

print(len(country_capitals))
print(country_capitals.get("Germany"))

print(country_capitals.keys())
print(country_capitals.values())

country_capitals["Ghana"] = "Accra"
print(country_capitals)
# print(f"{country_capitals.keys()[3]} : country_capitals.values()[3])