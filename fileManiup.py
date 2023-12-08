import shutil
import os
# #File Operations
# #Task 1: Done (downloaded sample.txt and added it)
# #Task 2
# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         content = file.read()
#         return content
# print(read_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/sample.txt"))
# #Task 3
def edit_text_file(file_path, new_content):
    with open(file_path, 'a') as file:
        return file.write(new_content)
# edit_text_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/sample.txt", "Additional line added for file operations.")

# #Folder Manipulation
# #Task 4
# def makeFolder(director, parent_dir):
#     os.makedirs(os.path.join(parent_dir, director))
#     print("Successfully Created.")
# makeFolder("Files", "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/")
# #Task 5
# shutil.move('sample.txt', 'C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files')

#File Manipulation
#Task 6
# edit_text_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/file1.txt", "Hi")
# edit_text_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/file2.txt", "Bye")
#Task 7
# def rename(source, de):
#     os.rename(source, de) 
#     print("Sucesfully renamed.")
# rename("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/file1.txt", "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/renamed_file.txt")
#Task 8
# os.remove("file2.txt")

#Additional Operations
#Task 9
def find_files_and_folders(path):
    for root, dir, files in os.walk(path):
        print(f"Current directory: {root}")
        print('Directories:')
        for directory in dir:
            print(os.path.join(root, directory))
        print('Files:')
        for file in files:
            print(os.path.join(root, file))
        print("------------------------")
find_files_and_folders("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files")
#Task 10
# shutil.make_archive('archive', 'zip', "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files")