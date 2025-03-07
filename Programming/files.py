import os
# Write a program to read text file
file = open("Programming/example.txt", 'r')
content = file.read()
print(content)
file.close()

# Write a program to write text to .txt file using InputStream
file = open('Programming/example.txt', 'w')
content1 = file.write("This is the second line")
print(content1)
file.close()

file = open('Programming/example.txt', 'r')
content2 = file.read()
print("File Contents: ")
print(content2)
file.close()

file = open('Programming/example.txt', 'r')
file.seek(5)
print(file.read(6))
file.close()

if os.access('Programming/example.txt', os.R_OK):
    print("File has read access")
if os.access('Programming/example.txt', os.W_OK):
    print("File has write access")
