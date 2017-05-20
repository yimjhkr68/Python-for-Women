# image_file2.py

import os


# Read files from the directory (binary mode)
dir_name =  r"C:\Temp"

file_names = os.listdir(dir_name)
print (file_names)


# filter non-image files
obj_files = []
for img_nm in file_names:
    if img_nm[-3::] == 'jpg':
        print (img_nm)
        obj_files.append(img_nm)

print (obj_files)
