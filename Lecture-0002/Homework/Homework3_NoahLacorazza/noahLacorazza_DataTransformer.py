# File: noahLacorazza_DataTransformer.py
# Author: Noah Lacorazza
# Date: 9/23/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# Asks the user to fill out a list. Then, using that list, gives info such as sum, average, number of odd numbers, etc
# Collaboration:
# N/A

data_len = int(input("Enter number of data points as a positive int: "))
data_list = list()
even_numbers = list()
odd_numbers = list()

data_range = range(data_len)
for i in data_range:
    # Fills the data via user input
    datum = int(input("Enter an integer: "))
    data_list.append(datum)

    # Finds the sum of the data
    data_sum += datum

    # Finds the data's minimum
    if data_min == None or datum < data_min:
        data_min = datum
    else: 
        # Finds the data's maximum
        if data_max == None or datum > data_max:
            data_max = datum
    
    # Creates and counts odd and even number lists
    if datum % 2 == 0:
        even_numbers.append(datum)
        even_count += 1
    else:
        odd_numbers.append(datum)
        odd_count += 1

# Finds the average of the data
data_avg = data_sum / data_len

# Prints all the information we used
print(f"""User list: {data_list}
Sum: {data_sum}
Average: {data_avg}
Minimum: {data_min}
Maximum: {data_max}
Even numbers: {even_count}
Even list: {even_numbers}
Odd numbers: {odd_count}
Odd list: {odd_numbers}""")