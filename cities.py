#!/usr/bin/python
import sys, math

class City:
	def __init__(self, index, xCoord, yCoord, distNext):
		self.index = index
		self.x = xCoord
		self.y = yCoord
		self.distNext = distNext

# Accepts a list of tuples of the type cities.
# Outputs a list of City objects.
def CityTupToObj(cityList):
	numCities = len(cityList)
	print "The number of cities in CitTupToObj " + str(numCities)

	cityListObjects = []

	for i in range(0, len(cityList)):
		cityListObjects.append(City(cityList[i][0], cityList[i][1], cityList[i][2], 0))

	return cityListObjects

# Quick function to print out the list of city objects after conversion from tuples.
def printObjCities(cities):
	print "The cities will be printed with the following columns."
	print "Index    X Coordinate    Y Coordinate  Distance to the next city to visit."
	for i in range(0, len(cities)):
		print str(cities[i].index) + "    " + str(cities[i].x) + "    " + str(cities[i].y) + \
		"    " + str(cities[i].distNext) 

# This function must take a city object as defined above.
def distNextCity(city, curCity, nextCity):
	print "Next city index: " + str(city[nextCity].index)
	print "Next city xCoord: " + str(city[nextCity].x)
	print "Next city yCoord: " + str(city[nextCity].y)
	print