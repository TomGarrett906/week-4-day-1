'''7KYU - AREA OF A CIRCLE 

Complete the function which will return the area of a circle with the given radius.

Returned value is expected to be accurate up to tolerance of 0.01.

If the radius is not positive, raise ValueError.

Example:

circle_area(43.2673)      # returns 5881.248  (± 0.01)
circle_area(68)           # returns 14526.724 (± 0.01)
circle_area(0)            # raises ValueError
circle_area(-1)           # raises ValueError
'''


#O(1) very efficient, just checking one thing
def circle_area(r): #O(1) constant

    area =  3.14 * (r**2)  #O(1) one iteration
    if r <= 0:  #O(1) one time
        raise ValueError("Invalid radius. Radius must be a positive value.") #O(1) just check once

    return area #O(1)  one time

print(circle_area(1)) #O(1) calling one thing