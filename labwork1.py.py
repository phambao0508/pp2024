#List functions:
students = []
courses = []
marks = {}


# input functions

# input students information in a class
def input_num_students():
    return int(input("Enter number of students: "))

def input_student_information():
    num_students = input_num_students()
    for _ in range(num_students):
        id_student = input("Enter student ID: ")
        name_student = input("Enter student name: ")
        dob_student = input("Enter student dob: ")
    # Store student information in a dictonary
        student = {
            "ID ": id_student,
            "Name ": name_student,
            "Dob ": dob_student
        }   
        students.append(student)
    return students

# input course information
def input_num_course():
    return int(input("Enter the number of the course: "))

def input_course_information():
    num_course = input_num_course()
    for _ in range(num_course):
        id_course = input("Enter the course ID: ")
        name_course = input("Enter the course name: ")
        course = {
            "ID " : id_course,
            "Name " : name_course
        }
        courses.append(course)
    return courses

# select course and input mark
def input_mark():
    id_course = input("Enter the course that you want to input mark: ")
    if (not any(course["ID"] == id_course for course in courses)):
        print("Invalid course!")
        return
    # Create a dictionary to store mark of a course ID
    marks[id_course] = {}
    # Input mark for each student
    for student in students:
        mark = float(input("Enter mark for student  " + student["Name"] + " ID: " + student["ID"] + ": ")) # student["Name"] +  ID:  + student["ID"] get Name and ID of the student that in dict student
        marks[id_course][student["ID"]] = mark 
# Show list of students
def list_student():
    for student in students:
        print("Student: ")
        print("ID: " + student["ID"] + " Name: " + student["Name"] + " Dob: " + student["Dob"])

# Show list of courses  
def list_course():
    for course in courses:
        print("Course: ")
        print("ID: " + course["ID"] + " Name: " + course["Name"])

# show student marks for a course:
def show_mark():
    id_course = input("Enter the course ID that you want to show mark: ")
    # Check if the course ID exists
    if id_course not in marks:
        print("No marks available for this course!")
        return
    # Print mark
    for student in students:
        id_student = student["ID"]
        if student["ID"] in marks[id_course]:
            print("Mark for the student " + student["ID"] + " Name: " + student["Name"] + "in this " + id_course + ": ")
def menu():
    while True:
        print("\n------ Menu ------")
        print("1. Input student information")
        print("2. Input course information")
        print("3. Input marks for a course")
        print("4. List all students")
        print("5. List all courses")
        print("6. Show marks for a course")
        print("7. Exit")

        choice = int(input("Enter your choice between 1 - 7 "))

        if (choice == 1):
            input_student_information()
        elif (choice == 2):
            input_course_information()
        elif (choice == 3):
            input_mark()
        elif (choice == 4):
            list_student()
        elif (choice == 5):
            list_course()
        elif (choice == 6):
            show_mark()
        elif (choice == 7):
            print("------Existing--------")
            break
        else: 
            print("Invalid choice, try again! ")
        continue

# Start the program   
menu()



    