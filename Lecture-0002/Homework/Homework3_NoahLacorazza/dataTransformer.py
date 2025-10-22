# THIS WAS MADE AS A SELF-CHALLENGE. NO GRADING

data_list = range(int(input("Enter length of your list as a positive integer: ")))
even_nums = list()
odd_nums = list()

for data in data_list:
    data = int(input("Enter an integer: "))

    if data % 2 == 0:
        even_nums.append(data)
    else:
        odd_nums.append(data)

print(f"""User list: {data_list}
Sum: {sum(data_list)}
Average: {sum(data_list) / len(data_list)}
Minimum: {min(data_list)}
Maximum: {max(data_list)}
Even list: {even_nums}
Even count: {len(even_nums)}
Odd list: {odd_nums}
Odd count: {len(odd_nums)}""")

# Solution given by a friend

data_list = [int(input("Enter an Integer: ")) for element in range(int(input("Number of data points: ")))]
even_nums = [element for element in data_list if element % 2 == 0]
odd_nums = [element for element in data_list if element % 2 != 0]

print(f"""User list: {data_list}
Sum: {sum(data_list)}
Average: {sum(data_list) / len(data_list)}
Minimum: {min(data_list)}
Maximum: {max(data_list)}
Even list: {even_nums}
Even count: {len(even_nums)}
Odd list: {odd_nums}
Odd count: {len(odd_nums)}""")
