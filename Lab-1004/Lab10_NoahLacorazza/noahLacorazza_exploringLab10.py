### Example 1 ###
names_file = open("Lab10_NoahLacorazza/names.txt", "r")
print(names_file)

for name in names_file:
    print(name)

### Example 2 ###

with open("names.txt", "a") as names_file:
    pass

# Question 1
    # yes
# Question 2
    # no

### Example 3 ###
with open("names.txt", "r") as names_file:
    for i in range(int(input("How many names would you like to add?: "))):
        new_name = input("Enter a name to add to the file: ")
        new_names = []
        new_names.append(new_name + "\n")

# Question 1
    # no
# Question 2
    # no

### Example 4 ###
with open("names.txt", "a") as names_file:
    names_file.write(str(new_names))