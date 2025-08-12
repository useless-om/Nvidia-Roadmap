# marks ={ "zoro":89,
#         "sani":69,
#         "robin":99}

# for crew,bodycount in marks.items():
#     print(f"{crew}'s bodycount is {bodycount}")



# Step 1: Create list of students (each as tuple)
students_list = [
    ("Om", 19, 95),
    ("Ravi", 20, 88),
    ("Asha", 18, 92)
]

# Step 2: Create dictionary with roll numbers as keys
students_dict = {}
for roll_no, student in enumerate(students_list, start=1):
    students_dict[roll_no] = student

# Step 3: Print all students
for roll_no, student in students_dict.items():
    name, age, marks = student  # tuple unpacking
    print(f"Roll No: {roll_no}, Name: {name}, Age: {age}, Marks: {marks}")
