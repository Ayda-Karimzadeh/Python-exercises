# Question: Write a script that detects and prints out your monitor resolution

from screeninfo import get_monitors

resolution = get_monitors()[0]

width = resolution.width
height = resolution.height

print(f"Width: {width}, Height: {height}")

# The get_monitors  method produces a list like [monitor(1920x1080+0+0),
#  monitor(1280x1024+-1280+-31)]  listing all the monitors connected to the computer.
#  Applying [0]  to that list gives the first monitor object out of the list.
#  Applying width  to that monitor, the object gives the width of the monitor,
#  and the same goes for the height  property.