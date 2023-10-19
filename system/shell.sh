#!/bin/bash

## a script that takes a CSV file with two columns (name and age) and outputs the average age of the people in the file?
# Check if the filename argument is provided
if [ -z "$1" ]
then
  echo "Please provide a filename as an argument."
  exit 1
fi

# Extract the age column from the CSV file and compute the average
total_age=0
num_people=0
while IFS=, read name age
do
  # Check if the age is a valid number
  if [[ "$age" =~ ^[0-9]+$ ]]
  then
    total_age=$((total_age + age))
    num_people=$((num_people + 1))
  fi
done < $1
average_age=$(bc -l <<< "$total_age / $num_people")

# Output the average age
echo "Average age: $average_age"

##  script that takes a directory path as input and outputs a list of the top 10 largest files in that directory?
#!/bin/bash

# Check if the directory path argument is provided
if [ -z "$1" ]
then
  echo "Please provide a directory path as an argument."
  exit 1
fi

# Change to the directory
cd $1 || { echo "Could not change to directory: $1"; exit 1; }

# List the files in the directory, sort by size in descending order, and output the top 10
du -a | sort -n -r | head -n 10


## a shell script that reads a list of filenames from a file and outputs the total number of lines across all the files
#!/bin/bash

# Check if the filename argument is provided
if [ -z "$1" ]
then
  echo "Please provide a filename as an argument."
  exit 1
fi

# Loop through the filenames in the file
total_lines=0
while read filename
do
  # Count the lines in the current file and add to the total
  num_lines=$(wc -l < $filename)
  total_lines=$((total_lines + num_lines))
done < $1

# Output the total number of lines
echo "Total number of lines: $total_lines"
