import os

path = input("Please enter a path: ")
files = os.listdir(path)

file_types = {}

for file in files:
    file_type = os.path.splitext(file)[1].lower()
    if file_type in file_types:
        file_types[file_type] += 1
    else:
        file_types[file_type] = 1

for file_type, count in file_types.items():
    print(f"{file_type}: {count}")
