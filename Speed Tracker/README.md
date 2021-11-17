The solution for Speed Tracker! 
```
import time

#Asks for all of the things needed for the calculation
speed_limit = float(input("Speed limit: "))
time_taken = float(input("Time taken: "))
distance = float(input("Enter distance: "))
speed = distance / time_taken

#Displays all of the information, {:.2f} means to format to 2 d.p.
print("Time taken: {:.2f} seconds".format(distance))
print("Distance: {:.2f}".format(distance))
print("Speed: {:.2f}".format(speed))
print(f"Speed limit: {speed_limit}")

if speed > speed_limit:
    print("You were breaking the speed limit!")
else: 
    print("You were under the speed limit!")
```
Yeilds an output of:
```
doomcow500@shush:~/projects$ python3 speed-tracker.py
Speed limit: 30
Time taken: 5
Enter distance: 100
Time taken: 100.00 seconds
Distance: 100.00
Speed: 20.00
Speed limit: 30.0
You were under the speed limit!
```
