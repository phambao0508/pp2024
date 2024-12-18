import math
import numpy as np
import curses

class Students:
    def __init__ (self, name_student, id_student, dob_student):
        self.__name = name_student
        self.__id = id_student
        self.__dob = dob_student

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}, DOB: {self.__dob}"

class Course:
    def __init__ (self, name_course, id_course):
        self.__name = name_course
        self.__id = id_course

    def get_name(self):
        return self.__name
    
    def get_id(self):
        return self.__id
    
    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}, DOB: {self.__dob}"

class Mark:
    def __init__(self):
        self.__marks = {}
        self.__gpa = {}

    def input_marks(self, students, courses):
        id_course = input("Enter the course ID: ")
        course_found = any(course.get_id() == id_course for course in courses)
        if not course_found:
            print("Invalid course ID!")
            return
        
        for student in students: #To input the marks of the student until the input is true, and the mark will be stored in self.__marks with the format round to 1 decimal
            while True:
                try:
                    mark = float(input(f"Enter mark for {student.get_name()} (ID: {student.get_id()}): "))
                    mark = math.floor(mark * 10) / 10
                    self.__marks[(id_course, student.get_id())] = mark
                    break
                except ValueError:
                    print("Invalid input! Please enter another number. ")
        

    
    def calculate_gpa(self, students, courses):
        print("\n Calculating GPA...")
        student_ids = [student.get_id() for student in students]
        gpa_array = np.zeros(len(student_ids)) # Initialize GPA array
        count_array = np.zeros(len(student_ids))  # To count marks for averaging

    # Function to pdate marks and courses
        for(course_id, student_id), mark in self.__marks.items(): 
            if student_id in student_ids:
                idx = student_ids.index(student_id)
                gpa_array[idx] += mark #sum the grade in the overal grade
                count_array[idx] += 1 #upgrade the marks for averaging
        
    # Function to calculate the GPA for each student:
        for i, student_id in enumerate(student_ids): 
            if count_array[i]>0: #Only count for student who has at least 1 course
                gpa = gpa_array[i] / count_array[i] #Average = sum / course
                self.__gpa[student_id] = round(gpa, 2)

    # Function to sort and organize the GPA   
        sorted_gpa = sorted(self.__gpa.items(), key = lambda x:x[1], reverse=True)
        print("\n ___GPA List(Descending)___")
        for student_id, gpa in sorted_gpa:
            print(f"Student ID: {student_id}, GPA: {gpa}")
    
    # Function to show mark:
    def show_marks(self, students, courses):
        id_course = input("Enter the course ID to show marks: ")
        print(f"\nMarks for course {id_course}:")
        for student in students:
            mark = self.__marks.get((id_course, student.get_id()))
            if mark is not None:
                print(f"{student.get_name()} (ID: {student.get_id()}): {mark}")
            else:
                print(f"{student.get_name()} (ID: {student.get_id()}): No mark")

class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def input_students(self):
        n = int(input("Enter the number of students: "))
        for _ in range(n):
            id_student = input("Enter student ID: ")
            name_student = input("Enter name: ")
            dob_student = input("Enter DOB: ")
            self.students.append(Students(name_student, id_student, dob_student))

    def input_courses(self):
        n = int(input("Enter the number of courses: "))
        for _ in range(n):
            id_course = input("Enter course ID: ")
            name_course = input("Enter course name: ")
            self.courses.append(Course(name_course, id_course))

    def menu(self):
        while True:
            print("\n--- Menu ---")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks")
            print("4. Calculate GPA")
            print("5. Show marks")
            print("6. Exit")
            choice = input("Choose: ")
            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.marks.input_marks(self.students, self.courses)
            elif choice == '4':
                self.marks.calculate_gpa(self.students, self.courses)
            elif choice == '5':
                self.marks.show_marks(self.students, self.courses)
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice!")

# Run the program
school = School()
school.menu()



