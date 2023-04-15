# FileType
What file types are in a folder and how many

----

### Here's how the program works:

1. The program prompts the user to enter a path.
2. The program uses the `os.listdir()` function to get a list of files in the directory.
3. The program creates an empty dictionary called `file_types`.
4. The program loops through each file in the directory and gets its file type using the `os.splitext()` function. It then converts the file type to lowercase to make sure it is consistent.
5. If the file type is already in the `file_types` dictionary, the program increments the count by 1. If the file type is not in the dictionary, the program adds it with a count of 1.
6. Finally, the program loops through the `file_types` dictionary and prints out each file type and its count.
