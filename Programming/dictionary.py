# 1. Create a Dictionary with at least 5 key value pairs of the Student ID and Name
students = {
    101: "Lucky",
    102: "Purna",
    103: "Nanda",
    104: "Sai kiran",
    105: "Guna"
}

# 1.1. Adding the values in dictionary
students[106] = "Mani"
students[107] = "Praveen"
students[108] = "Balu"
print("Dictionary after adding values:", students)

# 1.2. Updating the values in dictionary
students[102] = "Purnachandra"
print("Dictionary after updating a value:", students)

# 1.3. Accessing the value in dictionary
print("Accessing student with ID 103:", students[103])

# 1.4. Create a nested loop dictionary
nested_students = {
    "Class A": {101: "Lucky", 102: "Purna"},
    "Class B": {103: "Nanda", 104: "Sai kiran"}
}
print("Nested dictionary:", nested_students)

# 1.5. Access the values of nested loop dictionary
print("Students in Class A:", nested_students["Class A"])

# 1.6. Print the keys present in a particular dictionary
print("Keys in students dictionary:", students.keys())

# 1.7. Delete a value from a dictionary
del students[105]
print("Dictionary after deleting a value:", students)
