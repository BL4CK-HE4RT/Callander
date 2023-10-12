#!/usr/bin/python3
import calendar
import time

year = 2023
month = 10

cal = calendar.month(year, month)
no="\033[1;37m—\x1b[0m"
sh=str(f"{no}"*25)

while True:
    # Get the current time
    current_time = time.strftime("%H:%M:%S")

    # Clear the screen (for Termux)
    print("\033c")

    # Display the current time
    print(sh)
    print("    Time:", current_time)
    print (sh)
    print(cal)

    # Wait for 1 second before updating the time
    time.sleep(1)
    
