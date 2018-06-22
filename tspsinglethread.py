# Class for running a single threaded tour of the Traveling Salesman Problem.
import os, sys, copy, math
from collections import namedtuple

class TspSingleThread:
	# Single threaded tour.
	# Returns the total distance of the tour.
	# Returns the order of the cities as a list
	def tour(cities, startCity):
		#print("inside tour. . . . . . . . . . .  ..")
		#print(cities)
		
		localCities = copy.deepcopy(cities)
		tour = []
		tourDistance = 0
		#print("len(City): %s" % (len(localCities)))
		#print("startCity: " + str(startCity))

		curCity = localCities.pop(startCity) 
		# print(curCity)
		# print(cities)
		tour.append(curCity)

		while len(localCities) > 0:
			# Find next closest city in the localCities list./
			nextCity, distToNext, index = TspSingleThread.nextCityDist(localCities, curCity)
			#print("nextCity: " + str(nextCity))

			# print("localCities length: %s" % len(localCities))
			# tour.append(localCities[0])
			
			tour.append(nextCity)
			localCities.pop(index)
			tourDistance += distToNext

		# print(tour)
		return tourDistance, tour

	# Find distance to the next closest city
	# Returns the distance to the next city and the ID of the next cloest city.
	def nextCityDist(localCities, curCity):
		distToNext = sys.maxsize
		curClosest = sys.maxsize 
		#print("nextCityDist() curCity: " + str(curCity))

		# Iterate over the existing cities
		for i in range(len(localCities)):
			curId = curCity.id
			curX = curCity.x
			curY = curCity.y

			# n is a prefix for next potential city.
			nx = localCities[i].x
			ny = localCities[i].y
			nid = localCities[i].id

			curClosest = math.sqrt((nx*nx) + (ny*ny))
			if distToNext > curClosest:
				distToNext = curClosest
				nextCity = localCities[i]
				index = i

		return nextCity, distToNext, index

	# wrapper loop that takes iterates over the import cases and passes in the start ID
	# Returns a list with all of the tours and shortest tour.
	def singleThreadedTsp(cities):
		# print(cities)
		shortestDist = sys.maxsize
		curDistance = sys.maxsize
		curTour = []
		shortestTour = []
		results = [] # May not be needed

		#print(shortestTour)
		for i in range(len(cities)):
			curDistance, curTour = TspSingleThread.tour(cities, i)
			#print("curTour: " + str(curTour))
			# print("curDistance: " + str(curDistance))
			curTour.insert(0, curDistance)
			results.append(curTour)
			if curDistance < shortestDist:
				shortestDist = curDistance
				shortestTour = curTour

		#sprint("shortestDist: " + str(shortestDist))
		# print("shortestTour: " + str(shortestTour))
		#print("results: ")
		#print(results)
		return results