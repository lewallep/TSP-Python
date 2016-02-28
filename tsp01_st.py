#!/usr/bin/python
import sys, math, re, time, copy, os
import cities

# This group of classes encapsulates my distance finding algorithm
# for a single threaded environment.  

def singleThreadedTour(cityList):
	numCities = len(cityList)
	nextCityIndex = 0

	# Reforactoring to change all of the cities to individual objects instead of tuples so the distance
	# To the next city can be saved in the object.
	cityListObj = cities.CityTupToObj(cityList)

	# Test print function only
	# cities.printObjCities(cityListObj)


	# Variables to keep track of tour length.
	curTour = sys.maxint
	bestTourSoFar = sys.maxint

	# Iterate through all of the different cities to find if there is a best starting position.
	for i in range(0, numCities):
		curStartCity = i
		citiesNotVisited = copy.deepcopy(cityListObj)
		# For each start position find the best tour.
		while len(citiesNotVisited) > 0:
			curCity = curStartCity
			
			for potentialNextCity in range(0, len(citiesNotVisited)):
				if potentialNextCity == curCity:
					print "I have found the current city and am skipping over it"
					print "The value of j is: " + str(potentialNextCity)
					potentialNextCity += 1
				else:
					print "else curCity: " + str(curCity)

					cities.distNextCity(citiesNotVisited, curCity, potentialNextCity)

			del citiesNotVisited[len(citiesNotVisited) - 1]
			print "citiesNotVisited len: " + str(len(citiesNotVisited))
			print
		print "At the end of the outer loop."