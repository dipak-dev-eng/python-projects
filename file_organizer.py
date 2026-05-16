import os
import shutil

source_folder = "test_folder"

file_types = {
    ".jpg": "Images",
    ".png": "Images",
    ".txt": "Documents",
    ".pdf": "Documents",
    ".py": "Python_Code"
}

for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1]

        folder_name = file_types.get(ext, "Others")
        target_folder = os.path.join(source_folder, folder_name)

        os.makedirs(target_folder, exist_ok=True)

        shutil.move(file_path, os.path.join(target_folder, file))

print("Files organized successfully!")