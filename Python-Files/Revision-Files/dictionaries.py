# A Dictionary is a bit more dynamic than Tuples and Lists, its a data collection
# Very useful tool within any coding language
# Simple concept of KEY and VALUE pairs {Key : Value}

# Syntax - We use { } to create a dictionary and Key : value for storing data

# Example ~
# name [Key] and John Byrne [Value]
# You can also have a List as a value
student_record = {
    "name": "John Byrne",
    "stream": "DevOps",
    "topics_completed": 5,
    "completed_lessons_name": ["Strings", "Tuples", "Variables"]
}

# Print out Dictionary and get the type <class 'dict'>
print(student_record)
print(type(student_record))

# Sorted the keys in this dictionary in alphabetical order
print(sorted(student_record))

print()  # Space in terminal

# Print out the values of the dictionary
print(student_record.values())

# Print out the values of the dictionary
print(student_record.keys())

print()  # Space in terminal

# Get value of a key from the dictionary "John Byrne"
# Change value of a keys value "James Bond"
print(student_record.get("completed_lessons_name")[1])
student_record["name"] = "James Bond"
print(student_record["name"])

# Add to the list inside our dictionary
student_record["completed_lessons_name"].append("Lists")
student_record["completed_lessons_name"].append("built-in methods")

# Add Item to the dictionary
student_record["Status"] = "In Progress"
print(student_record)

# Prints out the dictionary as a collection of Lists
print(student_record.items())

# Fetch a value from the key "completed_lessons_name" in the value which is a list at its index [1]
print(student_record["completed_lessons_name"][1])  # Tuples
print(student_record["completed_lessons_name"][2])  # Variables
