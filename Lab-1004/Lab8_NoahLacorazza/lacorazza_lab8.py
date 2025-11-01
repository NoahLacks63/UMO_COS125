#### Exercise 1 ####

student_scores = {
    "Alice" : 85,
    "Bob" : 92,
    "Charlie" : 78
}

print(student_scores["Bob"])

student_scores["Charlie"] = 88

student_scores["Dana"] = 95

print(student_scores)

#### Exercise 2 ####

city_data = {
    "Tokyo" : {
        "population" : 13900000,
        "country" : "Japan"
    },
    "Paris" : {
        "population" : 2140000,
        "country" : "France"
    }
}

print(city_data["Tokyo"]["population"])
print(city_data["Paris"]["country"])

#### Exercise 3 ####

board = [
    ["X", "O", "X"],
    ["-", "X", "O"],
    ["O", "-", "X"]
]

print(board[1][2])

board[3][1] = "X"

print(board[3])

#### Exercise 4 ####

def get_course_details():
    course_name = input("Enter course name: ")
    maximum_enrollment = int(input("Enter maximum enrollment: "))

    return tuple([course_name, maximum_enrollment])

course_name = get_course_details()[0]
maximum_enrollment = get_course_details()[1]

print(course_name, " ", maximum_enrollment)

#### Exercise 5 ####

student_roster = [
    {
        "student_id" : 1,
        "gpa" : 2.4,
        "major" : "CompSci"
    },
    {
        "student_id" : 2,
        "gpa" : 1.7,
        "major" : "Psych"
    },
    {
        "student_id" : 3,
        "gpa" : 5.0,
        "major" : "Bio"
    }
]

print(student_roster)

#### Exercise 6 ####

def create_assignment_record(name, max_points):
    assignment_info = {
        "AssignmentName" : name,
        "TotalPoints" : max_points,
        "DueWeek" : 5
    }

    return assignment_info

print(create_assignment_record("Lab1", 15))

#### Excercise 7 ####

def calculate_total_value(dictionaries):
    sum = 0
    for d in dictionaries:
        sum += d["price"]
    
    return sum

print(calculate_total_value([
    {
        "Name" : "Apple",
        "Price" : 5
    },
    {
        "Name" : "Eggs",
        "Price" : 99999
    },
    {
        "Name" : "Dog",
        "Price" : 40
    }
]))

#### Exercise 8 ####

student_list = [
    ["Noah", "A"],
    ["Brianna", "B"],
    ["Sarah", "C"],
    ["Jonah", "D"]
]

grade_counts = {
    "A" : 0,
    "B" : 0,
    "C" : 0,
    "D" : 0
}

for student in student_list:
    grade_counts[student[1]] += 1

print(grade_counts)

#### Exercise 9 ####

def popular_major(major_tally):
    