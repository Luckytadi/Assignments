class MyClass:
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor Called")
        elif arg2 is None:
            print(f"One Argument Constructor Called: {arg1}")
        else:
            print(f"Two Argument Constructor Called: {arg1}, {arg2}")


class Parent:
    def __init__(self, msg="Default Parent Constructor"):
        print(msg)


class Child(Parent):
    def __init__(self, msg="Default Child Constructor"):
        super().__init__("Calling Parent Constructor from Child")
        print(msg)


class AccessModifiers:
    def __init__(self):
        print("Public Constructor Called")

    def _protected_constructor(self):
        print("Protected Constructor Called")

    def __private_constructor(self):
        print("Private Constructor Called")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Person Created: {self.name}, {self.age} years old")

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")


def main():
    obj1 = MyClass()
    obj2 = MyClass("argument1")
    obj3 = MyClass("argument1", "argument2")

    obj_child = Child("Child Class Constructor")

    obj_access = AccessModifiers()
    obj_access._protected_constructor()
    print(dir(obj_access))

    person1 = Person("Lucky", 22)
    person1.display()
    person1.name = "Purna"
    person1.age = 26
    person1.display()


main()
