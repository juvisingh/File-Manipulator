
# File Manipulator

The objective of this assignment is to practice and demonstrate proficiency in handling files and folders through a series of tasks involving common file operations, folder manipulations, and file manipulations.


## Usage/Examples (import os, shutil)
**Task 1:**
```python
No Code- sample.txt is downloaded and directly added to the github
```
**Task 2:**
```python
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        return content
print(read_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/sample.txt"))
}
```
This function is called read_file. It takes in the parameter of the file path (Ex. "C:/Users/userName/Documents/file) and opens the file internally. Then, it reads the file and returns its content. In the solution, the contents of sample.txt are being read.

**Task 3:**
```python
def edit_text_file(file_path, new_content):
    with open(file_path, 'a') as file:
        return file.write(new_content)
edit_text_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/sample.txt", "Additional line added for file operations.")
```
This function is called edit_text_file. It takes in the parameter of the file path (Ex. "C:/Users/userName/Documents/file) and the new content that is going to be edited into the file. Firstly, the function opens the file. Then, since the second paramter of open() is 'a', the output of the program will be appended to the previous output of that file. For example, if the file contained the words "Hi" and "Bye" is the new_content paramater, the file would now have the contents "HiBye". That is what this function is doing. In the solution, the sentence "Additional line added for file operations" is appended to the file.

**Task 4:**
```python
def makeFolder(director, parent_dir):
    if os.path.exists(f"{parent_dir}{director}"):
        print("Folder already exists.")
    else:
        os.makedirs(os.path.join(parent_dir, director))
        print("Successfully Created.")
makeFolder("Files", "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/")
```
This function creates a new folder in a chosen directory. The function takes in two paramaters, the name of the Folder and the directory path as to where it will be created. Firstly, the function checks if the folder is already present using the os library. If it is, the function returns "Folder already exists". If it doesn't exit, it uses the directory name and file name are joined together and then a directory is made for it (both done using the os library). The function outputs "Successfully Created" as an indication that the folder was created. In the solution, a folder named "Files" is created in the File-Manipulator folder inside of the Github folder, which is inside Documents.

**Task 5:**
```python
# shutil.move(file_name, directory) is the original function
shutil.move('sample.txt', 'C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files')
```
This function move() is imported from the shutil library. The function takes in the name of the file and the directory is will be moved to. It is pretty simple. It finds the chosen file and moves it to the directory indicated by the parameter. In the solution, the sample.txt file is moved to the Files folder, which is in the File-Manipulator folder.

**Task 6:**
```python
def edit_text_file(file_path, new_content):
    with open(file_path, 'a') as file:
        return file.write(new_content)
edit_text_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/file1.txt", "Hi")
edit_text_file("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/file2.txt", "Bye")
```
This function is called edit_text_file. It takes in the parameter of the file path (Ex. "C:/Users/userName/Documents/file) and the new content that is going to be edited into the file. Firstly, the function opens the file. Then, since the second paramter of open() is 'a', the output of the program will be appended to the previous output of that file. For example, if the file contained the words "Hi" and "Bye" is the new_content paramater, the file would now have the contents "HiBye". That is what this function is doing. In the solution, the first file (file1.txt) has the word "Hi" appended to it. Then, the second file (file2.txt) has the world "Bye" appended to it.

**Task 7:**
```python
def rename(source, de):
    os.rename(source, de) 
    print("Sucesfully renamed.")
rename("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/file1.txt", "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/renamed_file.txt")
```
The function is called rename. It does exactly what it sounds like. It takes in the directory of the file (which is going to be renamed) and the future directory of the file after it is renamed. The rename function is imported from os and it renames the file. Once it has been done, the program tells the user that it has been "successfully renamed". For example, in the solution, the directory of file1.txt is taken in. Then, the future diectory of the file (which is the exact same but the file is now name renamed_file.txt) is taken in as the second parameter. The code executes and renames the file successfully.

**Task 8:**
```python
# os.remove(file_name) is the original function
os.remove("file2.txt")
```
This function is simple and straight from the os library. It takes in the name of the file and finds it. Then, it removes the file and deletes it. In the solution, file2.txt is deleted/removed from the directory.

**Task 9:**
```python
def find_files_and_folders(path):
    for root, dir, files in os.walk(path):
        print(f"Current directory: {root}")
        print('Directories:')
        for directory in dir:
            print(os.path.join(root, directory))
        print('Files:')
        for file in files:
            print(os.path.join(file))
        print("------------------------")
find_files_and_folders("C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files")
```
This function is called find_files_and_folders. The only parameter is the directory path. From the path, the function first prints the given directory. Then, it goes through the sub directories. This is done using os.path.join(). The files in the directory given are printed by using the same function as well. It prints them out and formats it with a horizontal line. In the solution, the function goes through "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files" and prints out the file names and sub directories (however, there is none).

**Task 10:**
```python
# shutil.make_archive('my_archive', 'zip', 'directory_to_archive') is the original function
shutil.make_archive('archive', 'zip', "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files")
```
This function is pulled from the shutil library. The first parameter is the name of the zip folder that will be created. The second parameter is zip, indicating what type of file to create. The last parameter is the directory path to the file/folder that is going to be zipped. In the solution, the first parameter is called archive (this is the name of the zip) and the type of file is zip (indicated by the second parameter). Lastly, the directory "C:/Users/jsingh619/Documents/GitHub/File-Manipulator/Files". Thus, the Files folder is being zipped into a file named archive.zip.
