# exif_read2.py

import exifread

# Open image file for reading (binary mode)
path_name =  "C:\Temp\pmp.jpg"
f = open(path_name, 'rb')

# Return Exif tags
tags = exifread.process_file(f)

#print (tags)
print (tags.get('EXIF DateTimeOriginal'))
datetime_st = str(tags.get('EXIF DateTimeOriginal'))

new_fn = ''
for char in datetime_st:
    if char not in { ' ', ':'}:
        new_fn = new_fn + char
new_fn = new_fn + '.jpg'
print (new_fn)
