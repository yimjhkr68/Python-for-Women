# file_rename1.py

import os

path = r"C:\Temp"
print (os.listdir(path))

os.chdir(path)

os.rename("sample.txt", "samlex.txt")

print (os.listdir(path))
