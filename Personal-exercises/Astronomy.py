# Question:Use Python to calculate the distance in kilometers between Jupiter and Sun on January 1, 1230.

import ephem

date = "1230/01/01"

jupiter = ephem.Jupiter()
jupiter.compute(date)

distance_au = jupiter.sun_distance

distance_km = distance_au * 149597870.691

print(distance_km)