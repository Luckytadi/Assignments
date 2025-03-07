class A():
    instance_variable = "Alphabet A"

    def first_alphabet(self):
        return 'A is the first alphabet'

    def method_of_A(self):
        return 'This is a method in A'

    def grade(self):
        return 'A is used as a grade'


class B(A):
    instance_variable = "Alphabet B"

    def second_alphabet(self):
        return 'B is the second alphabet'

    def method_of_B(self):
        return 'This is a method in B'

    def grade(self):
        return 'B is also used as a grade'


class C(B):
    instance_variable = "Alphabet C"

    def third_alphabet(self):
        return 'C is the Third alphabet'

    def method_of_C(self):
        return 'This is a method in C'

    def grade(self):
        return 'C is also used a grade'


class Main():
    @staticmethod
    def main():
        obj_A = A()
        obj_B = B()
        obj_C = C()

        print(obj_A.first_alphabet())
        print(obj_A.grade())
        print(obj_A.method_of_A())

        print(obj_B.second_alphabet())
        print(obj_B.grade())
        print(obj_B.method_of_B())

        print(obj_C.method_of_C())
        print(obj_C.third_alphabet())
        print(obj_C.method_of_C())

        ref_A: A = obj_B
        print(ref_A.grade())
        ref_A = obj_C
        print(ref_A.grade())

        print(f"Instance_variable of A: {obj_A.instance_variable}")
        print(f"Instance_variable of B: {obj_B.instance_variable}")
        print(f"Instance_variable of C: {obj_C.instance_variable}")


Main.main()
