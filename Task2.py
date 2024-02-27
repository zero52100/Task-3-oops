import os
class File_operation:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
    def __enter__(self):
        self.file = open(self.file_name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if 'bug' in open(self.file_name).read() or exc_type is not None:
            print(f"Deleted  file: {self.file_name}")
            try:
                os.remove(self.file_name)
            except FileNotFoundError:
                pass 
file_name = input("Enter filename: ")

with File_operation(file_name) as file:
    user_input = input("Enter text to write to file: ")
    file.write(user_input)
