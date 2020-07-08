class TextFileHandler:

    def __init__(self, __file_path, __text_storage=None):  # This is the init, taking in a text file and path
        self.__file_path = __file_path
        self.__text_storage = __text_storage

    # This class is able to read in two ways and write in two ways
    def read_text_file(self):
        try:  # If there is an error opening the file go to the exception block ~
            file = open(self.__file_path, 'r')  # open file / 'r' = read mode
        except Exception as e:  # alias the error in e and print it out, return - catches the exception (error)
            return e
        else:  # If no error then do this code, and move onto finally block
            self.__text_storage = file.read()  # read the file
            # self.text_storage = file.read(3)  # It reads the first 3 characters in the text file
            # This reads the current line of the file (can be repeated below for each line)
            # file.seek(0)  # This tells the pointer to start at a certain position in the file
            # self.text_storage = file.readline()
            # self.text_storage = file.readline()
            # self.text_storage = file.readline()
            # This returns the last character it has read last, this also counts newlines and first character in newline
            print(file.tell())
            file.close()  # close the file / Important to close as it has a limit to how many files can be open at once
        finally:  # this will always run no matter what
            return self.__text_storage

    def write_text_file(self):
        # 'x' is also a function to create a file, however will return an error if the file already exists
        file = open("receipt.txt", "w")  # write file / 'w' is write
        # file = open("Receipt.txt", "a")  # append file / 'a' is append if you do 'a+' it includes read too
        # file.write("Receipt:\nSashima - 25.00\nRamen Noodles - 12.00")  # write this text to a file called Receipt.txt
        file.write("\n8 Onigiri 9.00\nPork Dumplings")  # this is a append file write instead to add on
        file.close()  # close file too
        print("Files has been closed : " + file.closed.__str__())  # gives the status of closure
        print("Current file is called : " + file.name)  # gives name of current file
        print("This file is in '" + file.mode + "' mode")  # gives mode of your current operation on the file
        return self.__text_storage

    def read_text_file_using_with(self):
        # to reduce the overhead of closing files
        with open("order.txt", "r") as file:  # open file
            self.__text_storage = file.read()  # read file / automatically closes file during time of execution
            return self.__text_storage

    def write_text_file_using_with(self):
        with open("receipt.txt", "w+") as file:
            file.write("Receipt\nYou have not ordered anything yet sir.\nRegards Alan")
            # pointer is at character 63, therefore it needs to be reset
            print("Your pointer is at " + file.tell().__str__() + " in the file. Reset it... to do another operation "
                                                                  "like read.")
            file.seek(0)  # Reposition pointer at the first character in the file, which is 0
            # Pointer is now at the first index in the file E.G. the beginning
            print("Pointer reset to " + file.tell().__str__() + "\n")
            self.__text_storage = file.read()  # You have written it therefore the pointer is at the end of the file
            return self.__text_storage

    def playing_with_python_os_module(self):
        import os  # local import in this methods scope
        print(os.getcwd())  # get current working directory - D:\SpartaGlobalRepo\Python-Files\File-Handling
        print(os.listdir())  # print out files in the current directory
        # This will rename the first file, to the name of the last file.
        # os.rename("receipt.txt", "expired_receipt.txt")  # os.rename(existing_file, new_file_name)
        # os.chdir("D:/")
        # print(os.getcwd())  # this gets the directory that was previously assigned to the chrdir in previous line
        # print(os.listdir())
        # os.mkdir("John")  # Create a directory
        # os.rmdir("John")  # Remove a directory

    def playing_with_exceptions(self):
        try:  # Try do the first bit of code E.G. open file
            file = open(self.__file_path, 'r')  # file is attempted to be opened
        except Exception as e:  # incorrect syntax so exception was raised
            print(e)  # print out the error, usually its better to print it out in english
            print("File is not present")
        else:  # else is the code that runs if there is no exception
            self.__text_storage = file.readline()
            file.close()
        finally:  # print out the code in the finally block
            return self.__text_storage

