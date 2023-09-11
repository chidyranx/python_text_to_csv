# python_text_to_csv


# Article to CSV Converter

## Overview

This Python script is designed to read text files from a specified folder and write their content into a CSV file. Each row in the CSV file represents one article, with the article name in the first column and the article content in the second column.

## Requirements

- Python 3.x
- Access to the folder containing the text files

## How to Use

1. Save the Python script in a location of your choice.
2. Open a terminal and navigate to the folder where the script is saved.
3. Run the script by executing `python script_name.py` (replace `script_name.py` with the name you gave to the script).

## Code Explanation

### Importing Modules

```python
import os
import csv
```

- `os`: Provides a way of interacting with the operating system, used here for file and directory operations.
- `csv`: Allows the script to read and write CSV files.

### Setting the Folder Path

```python
folder_path = "folder_path\\name"
```

- Specifies the folder path where the text files are located.

### Initializing Data Storage

```python
article_data = []
```

- Initializes an empty list to store the article data.

### Looping Through Files

```python
for filename in os.listdir(folder_path):
```

- Loops through each file in the specified folder.

### Checking File Type

```python
if filename.endswith(".txt"):
```

- Checks if the current file is a text file.

### Reading Text Files

```python
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()
```

- Opens and reads the content of each text file.

### Removing `.txt` Extension

```python
filename_without_extension = filename.replace('.txt', '')
```

- Removes the `.txt` extension from the filename.

### Storing Data

```python
article_data.append([filename_without_extension, content])
```

- Appends the filename and content to the `article_data` list.

### Writing to CSV

```python
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for row in article_data:
        csvwriter.writerow(row)
```

- Writes the `article_data` to a CSV file.

---

**Disclaimer**
---
This script is provided "as is" without any warranties or guarantees. The user assumes all responsibility for any data loss, damage, or other consequences that may arise from the use of this script. Always make sure to back up your data and test the script in a controlled environment before using it for important tasks.
