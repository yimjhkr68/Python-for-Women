# imgfile_naming.py
import os


# Read files from the directory (binary mode)
dir_name =  r"C:\Temp"
file_names = os.listdir(dir_name)
print ("All files : \n", file_names)

# filter non-image files
obj_files = []
for img_nm in file_names:
    if img_nm[-3::] == 'jpg':
        obj_files.append(img_nm)
print ("Image files : \n", obj_files)

# read EXIF
import exifread
new_files = []
for img_fn in obj_files:
    os.chdir(dir_name)    
    f = open(img_fn, 'rb')
    tags = exifread.process_file(f)
    f.close()

# capture datetime from EXIF
    datetime_st = str(tags.get('EXIF DateTimeOriginal'))
# filter files not having EXIF
    if datetime_st == 'None':
        continue

# generate new file name using EXIF
    new_fn = ''
    for char in datetime_st:
        if char not in { ' ', ':', '.'}:
            new_fn = new_fn + char
    new_files.append([img_fn, new_fn])

print ("Image files having EXIF: \n", new_files)

# resolve same file name
i = 0
for fn1 in new_files:
    i = i+1
    rep_count = 0
    j = 0
    for fn2 in new_files[i::]:
        if fn1[1] == fn2[1]:
            print (fn1[1], fn2[1])
            rep_count = rep_count + 1
            new_files[i+j][1] = new_files[i+j][1] + '(' + str(rep_count) + ')' + '.jpg'
        j = j+1
print (new_files)    
# rename image file
for f in new_files:
    os.rename(f[0], f[1])

print (os.listdir(dir_name))

    
