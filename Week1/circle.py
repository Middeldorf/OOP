import math

# Read radius from user
radius_str = input ("Enter the radius of your circle: ")

# Convert radius to integer
radius_int = int(radius_str)

# Calculate circumference
circumference = 2 * math.pi / radius_int

# Calculate area
area = math.pi * (radius_int ** 2)

print "The circumference is:", circumference,", and the area is: ", area


