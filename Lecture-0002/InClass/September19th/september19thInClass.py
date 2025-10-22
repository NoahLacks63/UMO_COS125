CUTOFF = 13
YES = "yes"

age = int(input("Enter your age: "))

if age < CUTOFF:
    if input("Do you have parental consent? (yes or no): ") != YES:
        print("You cannot watch the movie")
    else:
        print("You can watch the movie")
else:
    print("You can watch the movie")