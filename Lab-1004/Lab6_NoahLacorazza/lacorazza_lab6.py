user_int = int(input("Enter a positive integer: "))

number_list = []

i = 0
while i < range(user_int):
    number_list.append(int(input("Enter an int: ")))
    i += 1

for i in range(user_int):
    number_list[i] = int(input("Enter an int: "))

data_list = input("Enter a list of numbers separated by commas: ").split(",")

for i in range(len(data_list)):
    data_list[i] = int(data_list[i])

sum = 0
for n in data_list:
    sum += n

sum = 0
i = 0
while i < len(data_list):
    sum += data_list[i]
    i += 1

average = sum / len(data_list)

min = None
max = None
for n in data_list:
    if min == None or n < min:
        min = n
    
    if max == None or n > max:
        max = n

even_numbers = []
odd_numbers = []

for n in data_list:
    if n % 2 == 0:
        even_numbers.append(n)
    else:
        odd_numbers.append(n)

even_len = len(even_numbers)
odd_len = len(odd_numbers)

print(f"""{data_list}
Sum: {sum}
Average: {average}
Min: {min}
Max: {max}
Evens: {even_numbers}
Even length: {even_len}
Odds: {odd_numbers}
Odd length: {odd_len}""")