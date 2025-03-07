# 1. Write a program to generate Arithmetic Exception without exception handling
import os
# print(10 / 0)

# 2. Handle the Arithmetic exception using try-catch block
try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("Exception caught:", e)

# 3. Write a method which throws exception, Call that method in main class without try block


def throw_exception():
    raise ValueError("This is an exception")


throw_exception()

# 4. Write a program with multiple catch blocks
try:
    x = int("hello")
except ValueError:
    print("Caught ValueError")
except TypeError:
    print("Caught TypeError")

# 5. Write a program to throw exception with your own message
raise Exception("This is a custom exception message")

# 6. Write a program to create your own exception


class MyCustomException(Exception):
    pass


raise MyCustomException("This is my custom exception")

# 7. Write a program with finally block
try:
    print(10 / 2)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This will always execute")

# 8. Write a program to generate Arithmetic Exception
print(5 / 0)

# 9. Write a program to generate FileNotFoundException
if not os.path.exists("non_existent_file.txt"):
    raise FileNotFoundError("File not found")

# 10. Write a program to generate ClassNotFoundException
try:
    import nonexistentmodule
except ModuleNotFoundError as e:
    print("Class not found exception:", e)

# 11. Write a program to generate IOException
try:
    with open("readonly_file.txt", "w") as file:
        file.write("This will fail if the file is read-only.")
except IOError as e:
    print("IOException caught:", e)

# 12. Write a program to generate NoSuchFieldException


class Sample:
    existing_field = "I exist"


try:
    print(getattr(Sample, "non_existent_field"))
except AttributeError as e:
    print("NoSuchFieldException caught:", e)
