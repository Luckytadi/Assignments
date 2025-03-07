class static_variable_class():
    static_variable = 10


obj = static_variable_class()
print(
    f"Accessing static variable through a class: {static_variable_class.static_variable}")
print(f"Accessing static variable through a instance: {obj.static_variable}")
obj.static_variable = 20
print(
    f"Changing static variable within the instance and accessing it through a instance: {obj.static_variable}")
static_variable_class.static_variable = 30
print(
    f"Changing static variable within the class and accessing it through a class: {static_variable_class.static_variable}")
