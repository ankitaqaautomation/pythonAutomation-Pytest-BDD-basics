# This file demonstrates the use of parameterized constructors and static methods in Python classes.

class Student:
    college = "SBES Aurangabad"

    # default constructor
    def __init__(self):
        self.studName = "Unknown"
        self.studSubject = "Unknown"
        self.studMarks = 0


    # parameterized constructor
    def __init__(self, name, subject, marks):

        self.studName = name
        self.studSubject = subject
        self.studMarks = marks

# class method

    @staticmethod        # decorator
    def calculate_grade(marks):

        if marks>=90:
            return "A Grade"
        elif marks>=75:
            return "B Grade"
        elif marks>=60:
            return "C Grade"
        elif marks>=40:
            return "Grade D"
        elif marks<40:
            return "Failed"
        
  # decorater is a method/function that wraps another function to extend its behavior without modifying the original function’s code.

    def get_StudentInfo(self):

        studentA = Student("Karan", "Maths", 89)
        print(studentA.studName)
        print(studentA.studSubject)
        print(studentA.studMarks)

print (Student.calculate_grade(76))
        
#Note:
# static method is a method that don't use the self parameter.
# static methods are at class level and not at object level. 
# static methods can be called using the class name without creating an instance of the class.
# A decoder converts encoded data → readable form.
# encode() → string → bytes
# decode() → bytes → string