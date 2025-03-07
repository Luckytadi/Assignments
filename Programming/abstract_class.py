from abc import ABC, abstractmethod


class abstract_class(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        return "This is a non-abstract method"


class sub_class(abstract_class):
    def abstract_method(self):
        return 'Abstract method is implemented in sub_class'

    def instance_method(self):
        return self.abstract_method()

    def sub_non_abstract_method(self):
        return self.non_abstract_method()


obj = sub_class()
print(obj.non_abstract_method())
print(obj.instance_method())
print(obj.sub_non_abstract_method())
