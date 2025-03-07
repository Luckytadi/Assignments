class student:

    name = None
    _no = None
    __group = None

    def __init__(self, name, no, group):
        self.name = name
        self._no = no
        self.__group = group

    def __private_method(self):
        return "This is a Private method"

    def access_private(self):
        return f"Accessing Private Field: {self.__group}\n Calling Private Method: {self.__private_method()}"


def main():
    obj = student("lucky", 31, "data Science")
    print(obj.access_private())


print(main())


class sub_class(student):
    def access_student(self):
        try:
            return f"accessing Super class Private Field: {self.__group}\n Calling Super Class Private Method{self.__private_method()}"
        except AttributeError:
            return "Cannot access private field from subclass"


sub_class = sub_class('Praveen', 28, 'Data Science')
print(sub_class.access_private())


class protected_class():
    def __init__(self):
        self._protected_field = "Protected Field"

    def _protected_method(self):
        return "This is a Protected Method"


class access_protected_class:
    def access_protected(self):
        obj1 = protected_class()
        return f"Accessing Protected Field: {obj1._protected_field}\nCalling Protected Method: {obj1._protected_method()}"


obj2 = access_protected_class()
print(obj2.access_protected())


class public_class:
    name = "Mani"
    no = 9

    def public_method(self):
        return "This is a public class"


obj1 = public_class()
print("Public flieds: ", obj1.name, obj1.no)
print("Public Method: ", obj1.public_method())
