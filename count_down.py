import os
import time

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%02d:%02d" % (minutes, seconds)

sesh = int(input("How many mineuets will your seshion be: \n",)) * 60
os.system('cls' if os.name == 'nt' else 'clear')
green = "\033[0;32m"
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

was = int(round(time.time()))
now = int(round(time.time()))
secs = now - was

while was + sesh != now:
    now = int(round(time.time()))
    secs = now - was
    txt = convert(sesh) + "/" +  convert(secs)
    
    print(green + '\r',txt.center(200), end='')

    
    
    time.sleep(1)