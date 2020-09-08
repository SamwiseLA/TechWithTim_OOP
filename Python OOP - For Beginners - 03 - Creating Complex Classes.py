# Everything is a class!
# Use type() to see it's class
# A Class is just the overall definition and methods of an object (OOP)
#

# Creating a Complex Class - like using class defined fields as attributes of a class
# In this case a student class is used as an attribute of class AND it is a list(table/array)
#

class Student:
    def __init__(self, name, age, grade):  # initialize Class Student with Values
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):  # Method inside of Class type Student
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # Store students in the class, and start it as a blank list

    def add_student(self, student):
        if len(self.students) < self.max_students:  # if number of current students > max_students
            self.students.append(student)  # add student given parameter (class type) to Course
            return True
        else:
            return False

    def get_average_grade(self):
        total_grade = 0
        for student in self.students:  # Loop through students enrolled in course and add up their GPA
            total_grade += student.get_grade()  # Student Class method used to get grade, in case field name change
        total_students = len(self.students)  # get number of students
        average_grade = total_grade / total_students  # get average GPA by dividing total GPA by number of students
        return average_grade


s1 = Student("Tom", 22, 92)
s2 = Student("Tim", 27, 77)
s3 = Student("Pete", 19, 85)
s4 = Student("Kathy", 18, 99)
s5 = Student("Heidi", 27, 75)

course = Course("History", 6)

as1 = course.add_student(s1)
as2 = course.add_student(s2)
as3 = course.add_student(s3)
as4 = course.add_student(s4)
as5 = course.add_student(s5)

avg = course.get_average_grade()

print(f"\nThe Course: [{course.name}] has {len(course.students)} students enrolled,"
      f" \nwith max enrollment of {course.max_students}\nThe Enrolled Students have a GPA"
      f" Average of {round(avg,1)}\n")
#  print levels
print(course)  # Print course instance
print(course.students)  # Print students list field in course
print("")
for stud in course.students:
    print(f"{stud.name} age: {stud.age}")  # Print every student name & age from students list field in course

print("\n--- End ---")
