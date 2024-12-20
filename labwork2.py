class Student:
    def __init__(self, name_student, id_student, dob_student):
        self.__name = name_student
        self.__id = id_student
        self.__dob = dob_student

    ## Encapsulation
    def get_name(self):
        return self.__name

    def set_name(self, name_student):
        self.__name = name_student

    def get_id(self):
        return self.__id

    def set_id(self, id_student):
        self.__id = id_student

    def get_dob(self):
        return self.__dob

    def set_dob(self, dob_student):
        self.__dob = dob_student

    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}, DOB: {self.__dob}"


class Course:
    def __init__(self, name_course, id_course):
        self.__name = name_course
        self.__id = id_course

    ## Encapsulation
    def get_name(self):
        return self.__name

    def set_name(self, name_course):
        self.__name = name_course

    def get_id(self):
        return self.__id

    def set_id(self, id_course):
        self.__id = id_course

    def __str__(self):
        return f"Name: {self.__name}, ID: {self.__id}"

#Function to input number of students and courses
class InputStudent:
    def input_number(self):
        while True:
            try:
                return int(input("Enter the number of students: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")


class InputCourse:
    def input_number(self):
        while True:
            try:
                return int(input("Enter the number of courses: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")


class Mark:
    def __init__(self):
        self.__marks = {}

    def get_marks(self):
        return self.__marks

    def set_marks(self, course_id, student_id, mark):
        self.__marks[(course_id, student_id)] = mark

    def input_marks(self, students, courses):
        id_course = input("Please enter the course ID: ")
        course_found = any(course.get_id() == id_course for course in courses)
        if not course_found:
            print("Invalid course ID!")
        
            return

        for student in students:
            while True:
                try:
                    mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_id()}): "))
                    if 0 <= mark <= 100:
                        self.set_marks(id_course, student.get_id(), mark)
                        break
                    else:
                        print("Mark should be between 0 and 100.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def show_marks(self, students, courses):
        id_course = input("Enter the course ID that you want to show marks for: ")
        print(f"\nMarks for course {id_course}:")
        for student in students:
            mark = self.get_marks().get((id_course, student.get_id()))
            if mark is not None:
                print(f"Student {student.get_name()} (ID: {student.get_id()}): {mark}")
            else:
                print(f"No mark found for student {student.get_name()} (ID: {student.get_id()}).")


class School:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = Mark()

    def input_student_information(self):
        student_input = InputStudent()
        num_students = student_input.input_number()
        for _ in range(num_students):
            id_student = input("Enter student ID: ")
            name_student = input("Enter student's name: ")
            dob_student = input("Enter student's DOB (YYYY-MM-DD): ")
            student = Student(name_student, id_student, dob_student)
            self.students.append(student)

    def input_course_information(self):
        course_input = InputCourse()
        num_courses = course_input.input_number()
        for _ in range(num_courses):
            id_course = input("Enter the course ID: ")
            name_course = input("Enter the course's name: ")
            course = Course(name_course, id_course)
            self.courses.append(course)

    def list_students(self):
        print("\nList of Students:")
        for student in self.students:
            print(student)

    def list_courses(self):
        print("\nList of Courses:")
        for course in self.courses:
            print(course)

    def menu(self):
        while True:
            print("\n------ Menu ------")
            print("1. Input student information")
            print("2. Input course information")
            print("3. Input marks for a course")
            print("4. List all students")
            print("5. List all courses")
            print("6. Show marks for a course")
            print("7. Exit")

            try:
                choice = int(input("Enter your choice between 1 - 7: "))
                if choice == 1:
                    self.input_student_information()
                elif choice == 2:
                    self.input_course_information()
                elif choice == 3:
                    self.marks.input_marks(self.students, self.courses)
                elif choice == 4:
                    self.list_students()
                elif choice == 5:
                    self.list_courses()
                elif choice == 6:
                    self.marks.show_marks(self.students, self.courses)
                elif choice == 7:
                    print("------ Exiting --------")
                    break
                else:
                    print("Invalid choice. Please choose between 1 and 7.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")


# Start the program
school = School()
school.menu()
