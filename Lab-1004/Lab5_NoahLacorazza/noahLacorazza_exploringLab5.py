# Example 1
converted_nums = []
numbers_list = input("Enter a list of 10 numbers separated by a space: ").split(" ")
print(f"The list is {numbers_list}. \nThe data type is {type(numbers_list)}")

for item in numbers_list:
    converted_nums.append(int(item))
    print(converted_nums)

print(f"The 4th element is: {numbers_list[3]} and is of type {type(numbers_list[3])}")
print(f"The 4th element is: {converted_nums[3]} and is of type {type(converted_nums[3])}")

# Example 2
my_range = range(0, 10, 2)
my_nums = list(range(0, 10, 2))
print(f"This is my_range: {my_range} and this is my_nums: {my_nums}")

# Example 3
listm = ["Hah!", 2, "3"]
for i in range(0, len(listm)):
    print(i)
    print(listm[i])

# Example 4
for letter in "this spring":
    print(letter)

saying = "this spring"
for letter in range(saying):
    print(saying[letter])

# Example 5
spot = 0
saying = "this spring"

while spot < len(saying):
    print(saying[spot])
    spot += 1

num_list = ["one", "two", "three", "four"]
x = 0
while x < len(num_list):
    print(x)
    x += 1

