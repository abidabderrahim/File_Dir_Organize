import os
import shutil

def organize_files(path):
    os.chdir(path)
    
    for filename in os.listdir(path):
        
        if os.path.isdir(filename):
            continue
        
        file_extension = os.path.splitext(filename)[1][1:]
        
        if not file_extension:
            continue

        if not os.path.exists(file_extension):
            os.makedirs(file_extension)

        shutil.move(filename, os.path.join(file_extension, filename))

path = input("Enter Directory Path : ")
organize_files(path)
