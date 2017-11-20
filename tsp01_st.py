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
	curTourDist = sys.maxsize
	bestTourSoFar = sys.maxsize
	nextStopDist = sys.maxsize

	# The list of cities visited for this particular tour.
	curTour = []
	nextBestDist = sys.maxsize
	cityTest = 0
	bestNeighborIndex = 0

	# Iterate through all of the different cities to find if there is a best starting position.
	for i in range(0, numCities):
		curTourDist = 0
		bestTourSoFar = sys.maxsize

		curStartCity = i 	#integer
		print("currentStartCity: " + str(curStartCity))
		print()
		citiesNotVisited = copy.deepcopy(cityListObj)
		curCity = curStartCity	# integer
		curTour.append(citiesNotVisited[curCity])
		curCityObj = citiesNotVisited[curCity]
		del citiesNotVisited[curCity]
		
		# For each start position find the best tour.
		while len(curTour) < numCities:
			# curTour.append(citiesNotVisited[curCity])
			while cityTest < len(citiesNotVisited):
				#print "Length citiesNotVisited beginning of loop: " + str(len(citiesNotVisited))
				#print "cities not visited curCity.index: " + str(citiesNotVisited[curCity].index)
				print("curCity: " + str(curCity))
				print("cityTest: " + str(cityTest))
				
				nextCityObj = citiesNotVisited[cityTest]
				dist = cities.distNextCityV2(curCityObj, nextCityObj)
				print("nextBestDist: " + str(nextBestDist))
				print("dist: " + str(dist))
				if dist < nextBestDist:
					nextBestDist = dist
					bestNeighborIndex = cityTest
					print("Found a closer neighbor.  Updated current best distance.")
					print("bestNeighborIndex = " + str(bestNeighborIndex))
					print()
				cityTest += 1
			
			curTour[len(curTour)-1].dist = nextBestDist
			curTour.append(citiesNotVisited[bestNeighborIndex])
			curTourDist += nextBestDist

			curCityObj = curTour[len(curTour)-1]
			nextBestDist = sys.maxsize
			curCity = bestNeighborIndex
			cityTest = 0
			dist = sys.maxsize
			print("bestNeighborIndex before delete: " + str(bestNeighborIndex))
			del citiesNotVisited[bestNeighborIndex]

			print("Length citiesNotVisited: " + str(len(citiesNotVisited)))
			for city in curTour:
				print(str(city.index) + "   " + str(city.x) + "   " +\
					str(city.y) + "   " + str(city.dist))

		# curTour.append(citiesNotVisited[0])
		print("curTour length: " + str(len(curTour)))
		curTour[len(curTour)-2].dist = cities.distNextCityV2(curTour[len(curTour)-2], curTour[len(curTour)-1])
		
		# Testing the length of the current tour
		print("number of cities: " + str(numCities))
		curTourDist += curTour[len(curTour)-2].dist

		for city in curTour:
			print(str(city.index) + "   " + str(city.x) + "   " +\
				str(city.y) + "   " + str(city.dist))


		print("curTourDist: " + str(curTourDist))
		print()
		# Resetting the tour list for the next start city.	
		curTour = []