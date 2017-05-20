### break_time2.py
import webbrowser
import time
# open web browser every 30 minute
current_time = time.ctime() # get current time
print ("start time = " + current_time)

# Number of Breaks
Num_Break = int(input('How many times do you want to break ? '))

# Interval of Breaks
Int_Min = int(input('Input break interval in minutes :'))

# Web link
url = input('Enter URL to enjoy : ')

i = 0
while(i<Num_Break):
    time.sleep(Int_Min * 60)
    webbrowser.open(url)
    i=i+1
    
