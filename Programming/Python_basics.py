Name = input()
print(Name)
# This is a single line comment.
'''
This is a multi line comment
'''
integer = 20
boolean = True
char = 'character'
float_value = 10.00
print(integer)
print(boolean)
print(char)
print(float_value)

x = 1000


def print_local_variable():
    x = 2000
    print(f"local variable: {x}")


print_local_variable()
print(f"global variable: {x}")
