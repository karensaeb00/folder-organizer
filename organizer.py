import os
import shutil

# Folder to organize (change this path to your own)
path = './test-folder'

file_types = {
    'Images': ['.jpg', '.png'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Videos': ['.mp4', '.mov'],
    'Scripts': ['.py', '.js']
}

for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file))
