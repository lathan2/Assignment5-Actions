import math

def firstrun():
    return "success"


def circle_area(radius):
    if (radius < 0):
        return -1
    
    else:
        return math.pi * math.pow(radius, 2)
