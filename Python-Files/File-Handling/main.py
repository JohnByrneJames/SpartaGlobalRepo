# Reading from and writing to files
from textfile import TextFileHandler

file_path = "order.txt"

text_file_object = TextFileHandler(file_path)

# Reading a file
# print(text_file_object.read_text_file())

# Writing a file
# text_file_object.write_text_file()

# Reading a file using the with function (exits overheads of closing)
# print(text_file_object.read_text_file_using_with())

print()

# writing a file using the with function
# print(text_file_object.write_text_file_using_with())

# text_file_object.playing_with_python_os_module()

# ___________________________

# print(text_file_object.playing_with_exceptions())

# Exceptions
# try [ Code to be run ~~ may raise an exception ]
# except (general / or pointed exception) [ do something to inform user of exception ]
# finally [ code that will always run finally, despite any exceptions ]

# If you have an error that is an exception then it will happen during runtime and cause the program to come to a
# abrupt exit. This is why we handle them with exceptions.

text_file_object.raise_exception()
