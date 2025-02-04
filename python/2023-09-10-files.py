import os
import datetime

# Specify the directory path you want to start from
directory_path = "/path/to/your/directory"

# Recursively iterate over all files in the directory and its subdirectories
for root, dirs, files in os.walk(directory_path):
    for filename in files:
        if filename.endswith(".md"):
            file_path = os.path.join(root, filename)

            # Get the file creation time
            creation_time = datetime.datetime.fromtimestamp(os.path.getctime(file_path))

            # Format the creation time in a specific way
            formatted_creation_time = creation_time.strftime("%Y-%m-%d %H:%M:%S")

            # Read the contents of the file with UTF-8 encoding
            with open(file_path, 'r', encoding='utf-8') as file:
                file_contents = file.readlines()

            # Check if the first lines contain the correct metadata
            if len(file_contents) >= 2 and file_contents[0].strip() == '---' and file_contents[1].startswith("File Creation Time:"):
                # File already contains the correct metadata, skip it
                continue
            else:
                # Check if the first line is '---'
                if len(file_contents) > 0 and file_contents[0].strip() == '---':
                    # If the first line is '---', insert the formatted date after it
                    file_contents.insert(1, f"File Creation Time: {formatted_creation_time}\n")
                else:
                    # If the first line is not '---', insert '---' and then the formatted date
                    file_contents.insert(0, '---\n')
                    file_contents.insert(1, f"File Creation Time: {formatted_creation_time}\n")

                # Write the updated contents back to the file with UTF-8 encoding
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.writelines(file_contents)

print("File creation times inserted successfully for .md files in all subdirectories!")
