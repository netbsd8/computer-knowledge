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
    for filename in filenames:
        print("Current Directory:", dirpath)
        print("Subdirectories:", dirnames)
        print("Files:", filenames)
        fullpath = os.path.join(dirpath, filename)
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


# read raw block
# Open() takes three parameters: a filename, the mode in which the file should be opened, and a buffer size.
# open will create the file is not existed
with open('text.txt', 'rb') as source_file:
    while True:
        chunk = source_file.read(1024)
        if not chunk:
            print("No data")
            break
        else:
            print(chunk)

# write
with open("writeable.txt", 'w') as f:
    f.write("text\nfile\n")
    f.writelines("%s\n" % i for i in range(10))
    f.close()


# Other os functions
os.chdir("/tmp")
os.mkdir("/tmp/os_mod_explore")
os.listdir("/tmp/os_mod_explore")
os.stat("/tmp/os_Mod_explore")
os.rename("/tmp/os_mod_explore/test_dir1", "/tmp/os_mod_explore/test_dir1_renamed")
os.rmdir("/tmp/os_mod_explore/test_dir1_renamed")
os.makedirs("test/test_subdir1/test_subdir2")
os.getcwd()
