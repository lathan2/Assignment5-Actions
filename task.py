# test file to unit test
import math
from datetime import date


def firstrun():
    return "success"


def circle_area(radius):
    if (radius < 0):
        return -1

    else:
        return math.pi * math.pow(radius, 2)


def first_last(arr):
    return arr[0], arr[-1]

def difference_dates(d1, d2):
    diff = d2 - d1
    return diff.days
