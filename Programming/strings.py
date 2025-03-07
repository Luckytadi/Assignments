import re
string1 = 'String one'
string2 = "String two"
string3 = '''String three'''
string4 = """this is also a string"""
string5 = 'hello world'
print(
    f"Different ways of creating strings:{string1, string2, string3, string4}")

print(
    f"concatenating string one and string two using '+' operator: {string1+string2}")

print(f"Length of string4 is {len(string4)}")

print(f"Extracting a substring: {string1[-3:]}")
print(f"Extracting a substring: {string3[-5:]}")

str1 = 'e'
str2 = 'two'
print("Position of e:", string1.index(str1))
print("Position of two:", string2.index(str2))

Substr = 'hello'
print(re.match(Substr, string5))
print(re.search('string', string4))

print("Comparing Strings: ")
print(string5 == string1)
print(string5 == string2)
print(string1 == string2)
print(string3 != string1)


print('startswith and endswith: ')
print(string5.startswith('hello'))
print(string5.endswith('world'))


string6 = 'good morning everyone'
print(string6.strip("everyone"))


print(string5.replace("Hello", "Hey"))


string7 = 'king-of-the-world'
print(string7.split("-"))


num = 10
str_num = str(num)
print(str_num)
print(type(str_num))


string8 = 'hello'
string9 = 'WORLD'
print(string8.upper())
print(string9.lower())
