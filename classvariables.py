# class variables = Shared among all instances of a class
#                   Defined outside the constructor
# Allows you to share data among all objects created from that class

class Student:

    class_year = 2026
    num_students = 0

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        Student.num_students += 1

student1 = Student("Spongebob",20)
student2 = Student("Patrick",19)
student3 = Student("Sandy",22)

print(f"My graduating class of {Student.class_year} has {Student.num_students} Students")
print(student1.name)
print(student2.name)
print(student3.name)