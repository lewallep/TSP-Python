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
	curTourDist = sys.maxint
	bestTourSoFar = sys.maxint
	nextStopDist = sys.maxint

	# The list of cities visited for this particular tour.
	curTour = []
	nextBestDist = sys.maxint
	cityTest = 0
	bestNeighborIndex = 0

	# Iterate through all of the different cities to find if there is a best starting position.
	for i in range(0, numCities):
		curTourDist = 0
		bestTourSoFar = sys.maxint

		curStartCity = i 	#integer
		citiesNotVisited = copy.deepcopy(cityListObj)
		curCity = curStartCity	# integer
		curTour.append(citiesNotVisited[curCity])
		curCityObj = citiesNotVisited[curCity]
		del citiesNotVisited[curCity]
		
		# For each start position find the best tour.
		while len(curTour) < len(citiesNotVisited):
			# curTour.append(citiesNotVisited[curCity])
			while cityTest < len(citiesNotVisited):
				print "Length citiesNotVisited beginning of loop: " + str(len(citiesNotVisited))
				#print "cities not visited curCity.index: " + str(citiesNotVisited[curCity].index)
				print "curCity: " + str(curCity)
				print "cityTest: " + str(cityTest)
				
				nextCityObj = citiesNotVisited[cityTest]
				dist = cities.distNextCityV2(curCityObj, nextCityObj)
				print "nextBestDist: " + str(nextBestDist)
				print "dist: " + str(dist)
				print
				if dist < nextBestDist:
					nextBestDist = dist
					bestNeighborIndex = cityTest
					print "Found a closer neighbor.  Updated current best distance."
					# print "bestNeighborIndex = " + str(bestNeighborIndex)
				cityTest += 1
			
			curTour[len(curTour)-1].dist = nextBestDist
			curTour.append(citiesNotVisited[bestNeighborIndex])
			curCityObj = curTour[len(curTour)-1]
			nextBestDist = sys.maxint
			curCity = bestNeighborIndex
			cityTest = 0
			nextBestDist = sys.maxint
			dist = sys.maxint
			del citiesNotVisited[bestNeighborIndex]

			print "Length citiesNotVisited: " + str(len(citiesNotVisited))
			for city in curTour:
				print str(city.index) + "   " + str(city.x) + "   " +\
					str(city.y) + "   " + str(city.dist)

		curTour.append(citiesNotVisited[0])
		curTour[len(curTour)-2].dist = cities.distNextCityV2(curTour[numCities-2], curTour[numCities-1])
		print
		for city in curTour:
			print str(city.index) + "   " + str(city.x) + "   " +\
				str(city.y) + "   " + str(city.dist)



		# Resetting the tour list for the next start city.	
		curTour = []