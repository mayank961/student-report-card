import os
import shutil

file_types ={
    'Images':['.jpg','.png','.jpeg','.gif'],
    'Documents':['.pdf','.docx','.txt'],
    'Songs':['.mp3','.wav'],
    'Videos':['.mp4','mov','.avi'],
    'Archives':['.zip','.rar','.tar','.gz'],
    'Scripts':['.py','.html','.js','.css'],
}

folder_path = input("Enter the folder path")

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)


    if os.path.isfile(file_path):
        ext = os.path.splitext(filename)[1].lower()

        moved = False

        for category, extensions in file_types.items():
            if ext in extensions:
                category_path = os.path.join(folder_path, category)
                os.makedirs(category_path, exist_ok=True)
                shutil.move(file_path, os.path.join(category_path, filename))
                print(f"Moved{filename} to {category}/")
                moved = True
                break
        if not moved:
            others_path = os.path.join(folder_path, 'others')
            os.makedirs(others_path, exist_ok=True)
            shutil.move(file_path,os.path.join(others_path, filename))
            print(f"moved {filename} to others/")
            