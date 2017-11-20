#!/usr/bin/python
import sys, math, re, time

# This function takes any type of object in a list, as long as it is a minMax object,
# and prints out the values in each list element.
# Prerequrisites
# Must use an instance of minMax
# minMax must be initialized.
class printSectors(object):
    def __init__(self, object):
        for i in range(0, len(object)):
            print("i = " + str(i))
            print("secMinX: " + str(object[i].secMinX))
            print("secMaxX: " + str(object[i].secMaxX))
            print("secMinY: " + str(object[i].secMinY))
            print("secMaxY: " + str(object[i].secMaxY))
            print

class printExtents(object):
    def __init__(self, object):
        print()
        print("MIN X : " + str(object.minX))
        print("MAX X : " + str(object.maxX))
        print()
        print("MIN Y : " + str(object.minY))
        print("MAX Y : " + str(object.maxY))
        print()

class printCities(object):
    def __init__(self, object):
        for city in object:
            print(str(city[0]) + "\t" + str(city[1]) + "\t" + str(city[2]))


def getDist(object):
    def __init__(self, object):
        x1 = loc1[0]
        x2 = loc2[0]
        y1 = loc1[1]
        y2 = loc2[1]
        dist = int(round(math.sqrt((X2 - x1)**2 + (y2 - y1)**2)))

        return dist

# Notes on Multithreading tsp01.py
# Import the list of cities.  
    #Done.
# Give each process it's own list to sort from memory
    
# Distribute the cities to their proper sectors. In each process.
#   This needs to be done in a way so each process is written the same.  
# Sort the cities for each sector in their own individual process.
# Define the start location.
# Combine the sorted cities depending on the start location.


## Attempt to not use locks when combining the sorted sector lists.