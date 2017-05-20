# exif_read1.py

import exifread

# Open image file for reading (binary mode)
path_name =  "C:\Temp\pmp.jpg"
f = open(path_name, 'rb')

# Return Exif tags
tags = exifread.process_file(f)

print (tags)
