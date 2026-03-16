# Question: Create a program that, once executed the programs prints Hello  instantly first, then it prints it after 1 second, then after 2, 3, and then the program prints out the message "End of the Loop" and stops.

# from time import sleep

# i=0
# while i<4:
#     i = i + 1
#     print("Hello")
#     sleep(i)

# print("End of the Loop ")

import time

i=0

while True:
    print("Hello")
    i = i + 1
    if i > 3:
        print("End of the Loop")
        break
    time.sleep(i)