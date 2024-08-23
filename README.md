
## Description

The File Organizer Tool is a Python script designed to organize files in a specified directory by their extensions. The tool automatically creates directories named after the file extensions (e.g., `.txt`, `.jpg`) and moves all files with the same extension into the corresponding directory. This helps keep your files neatly organized and easy to manage.

## Features

- Organizes files in a directory by their extension.
- Automatically creates directories for each file extension.
- Moves files into their respective extension-named directories.

## How It Works

1. **Change Directory**: The script starts by changing the working directory to the specified target directory.
2. **Iterate Over Files**: It then iterates through each file in the directory, ignoring subdirectories.
3. **Get File Extension**: For each file, the script extracts its extension.
4. **Create Directories**: If a directory for that extension doesn't exist, the script creates it.
5. **Move Files**: The file is then moved to the corresponding directory.

## Requirements

- Python 3.x
- `os` and `shutil` modules (these are part of the Python standard library, so no additional installation is required)

## How to Run

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using Python:

    ```bash
    python3 organize_files.py
    and enter your path directory
    ```
