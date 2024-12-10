course_code = input("Enter the course code: (e.g., \"CS101\", \"MATH202\", )")
student_grade = input("Enter your grade: ")

# Convert input to uppercase for case-insensitive comparison
course_code = course_code.upper()
student_grade = student_grade.upper()

# Extract the last three characters of the course code (use string slicing)
course_code_starting_index = len(course_code) - 3
course_suffix =  course_code[course_code_starting_index:]

# Check course code and grade to determine eligibility
if course_suffix == "101":
    if student_grade == "A" or student_grade == "B":
        print("You are eligible to enroll.")
    else:
        print("You are not eligible to enroll.")
elif course_suffix == "202":
    if student_grade == "B" or student_grade == "C":
        print("You are eligible to enroll.")
    else:
        print("You are not eligible to enroll.")
elif course_suffix == "303":
    if student_grade == "C" or student_grade == "D":
        print("You are eligible to enroll.")
    else:
        print("You are not eligible to enroll.")