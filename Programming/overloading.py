#  Python does not support method overloading in the same way as Java or C++

# Write two methods with the same name but different number of parameters of same type and call the methods
# This does not work in python
# Suitable ways
class find_area:
    def area(self, base, height=None):
        self.base = base
        self.height = height
        if self.height is None:
            return base ** 2
        return (self.base * self.height)/2


# Write two methods with the same name but different number of parameters of different data type and call the methods
# This as well does not work in python
# suitable ways
obj = find_area()
print(obj.area(30, 20))
print(obj.area(10))


class student:
    def result_CGPA(self, total_marks: int, roll_no: str):
        self.total_marks = total_marks
        self.roll_no = roll_no
        return f"{self.roll_no} has got {self.total_marks/100} CGPA"

    def result_Grade(self, Name: str, roll_no: int, grade: str):
        self.Name = Name
        self.roll_no = roll_no
        self.grade = grade
        return f"The student {self.Name} with roll number {self.roll_no} has achieved {self.grade} grade"


stud_obj = student()
print(stud_obj.result_CGPA(764, 31))
print(stud_obj.result_Grade("Lakshmi Narayana", 2246390045, "A"))


# Write two methods with the same name and same number of parameters of same type
# This as well won't work
class Test:
    def show(self, value: int):
        print(f"Method 1: Value is {value}")

    def show(self, value: int):  # This method overrides the previous one
        print(f"Method 2: Value is {value}")


obj = Test()
obj.show(10)
