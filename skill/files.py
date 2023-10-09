""" Dir operations
project/
│
├── main.py
│
├── utils/
│   ├── __init__.py
│   └── helper.py
│
└── data/
    ├── data1.csv
    └── data2.csv
"""

import os

# dirpath: A string representing the path to the directory.
# dirnames: A list of the names of the subdirectories in dirpath (excluding '.' and '..' which are special entries).
# filenames: A list of the names of the non-directory files in dirpath.
for dirpath, dirnames, filenames in os.walk("project"):
    print("Current Directory:", dirpath)
    print("Subdirectories:", dirnames)
    print("Files:", filenames)
    print("-----")

"""
Output:
Current Directory: project
Subdirectories: ['utils', 'data']
Files: ['main.py']
-----
Current Directory: project/utils
Subdirectories: []
Files: ['__init__.py', 'helper.py']
-----
Current Directory: project/data
Subdirectories: []
Files: ['data1.csv', 'data2.csv']
-----
"""

# count total number of lines within a folder
def count_lines_in_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        #  read a single line in memory
        #  in most modern file systems and operating systems, 
        #  the underlying I/O operations are buffered. 
        for line in f:
            count += 1
        return count
        #  #  readlines() loads the entire file into memory
        #  return len(f.readlines()) 

total_lines = 0

for dirpath, _, filenames in os.walk("project"):
    for filename in filenames:
        if filename.endswith(('.py', '.html')):
            file_path = os.path.join(dirpath, filename)
            total_lines += count_lines_in_file(file_path)

print(f"Total lines in .py and .html files: {total_lines}")