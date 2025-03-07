from access_modifiers import protected_class
from access_modifiers import public_class


class another_module(protected_class):
    def access_protected(self):
        return f"Accessing Protected Field: {self._protected_field}\nCalling Protected Method: {self._protected_method()}"


obj = another_module()
print(obj.access_protected())


class any_class:
    def access_protected(self):
        try:
            return f"Accessing Protected Field: {self._protected_field}\nCalling Protected Method: {self._protected_method()}"
        except AttributeError:
            return "Can only access protected class from the sub class"


obj2 = any_class()
print(obj2.access_protected())


class access_public(public_class):
    def access_public(self):
        return f"accessing Public flied: {self.name}\nAccessing Public Method: {self.public_method()}"


obj3 = access_public()
print(obj3.access_public())
