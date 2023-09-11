import os
import csv

# Define the folder path
folder_path = "file_path\\name"

# Initialize an empty list to store the article data
article_data = []

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a text file
    if filename.endswith(".txt"):
        # Create the full file path
        file_path = os.path.join(folder_path, filename)

        # Open and read the text file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Remove the '.txt' extension from the filename
        filename_without_extension = filename.replace('.txt', '')

        # Append the filename and content to the article_data list
        article_data.append([filename_without_extension, content])

# Write the article data to a CSV file
csv_file_path = "file_path\\articles.csv"
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write each article data as a row in the CSV file
    for row in article_data:
        csvwriter.writerow(row)

print("CSV file has been created.")
