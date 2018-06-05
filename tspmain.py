import os, sys, copy, math
from collections import namedtuple

# import the cities from the text file
# Returns a list of cities.  Cities = named tuple?
def importCase():
	cities = []
	City = namedtuple("City", ["id", "x", "y"])
	with open(sys.argv[1], "r") as f:
		line = f.readline().strip()
		tokens = line.split("\t")
		numcities = int(tokens[0])
		for i in range(numcities):
			line = f.readline().strip()
			tokens = line.split("\t")
			c = City(id = int(tokens[0]), x = int(tokens[1]), y = int(tokens[2]))
			cities.append(c)

	return cities


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
		nextCity, distToNext, index = nextCityDist(localCities, curCity)
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
	print("singleThreadedTsp()")
	# print(cities)
	shortestDist = sys.maxsize
	curDistance = sys.maxsize
	curTour = []
	shortestTour = []
	results = [] # May not be needed

	#print(shortestTour)
	for i in range(len(cities)):
		curDistance, curTour = tour(cities, i)
		#print("curTour: " + str(curTour))
		print("curDistance: " + str(curDistance))
		curTour.insert(0, curDistance)
		results.append(curTour)
		if curDistance < shortestDist:
			shortestDist = curDistance
			shortestTour = curTour

	#sprint("shortestDist: " + str(shortestDist))
	print("shortestTour: " + str(shortestTour))
	#print("results: ")
	#print(results)
	return results


# Ensure every city is only visited once in ONE tour the finished tour.
# Check for any duplicate ID's.
# Returns True if the results have no duplicate ID's.
def checkResultsAll(results):
	goodResults = False

	# Skip the tour distance at the beginning of each result
	for i in range(len(results)):
		tour = results[i]
		for city in range(1, len(tour)):
			print("city in tour: " + str(tour[city]))
		print(results[i][0])
		print()

	return goodResults

# Takes a tour and it's distance and checks to see if any of the edges 
# intersect each other.
# Only checks a subset of 4 connected vertexes at a time.
# Ideally this would be connected to the tours to identify and unwind intersections
# as the nearest neighbors are found.



# Finds and checks only the shortest tour from the list of results.
# Not especially fast as the results do not come back sorted in ascending order.
def checkResultShortest(results):
	bestDist = sys.maxsize
	bestIndex = None
	bestTour = []
	idDict = {}

	for i in range(len(results)):
		if results[i][0] < bestDist:
			bestDist = results[i][0]
			bestIndex = i

	bestTour = results[bestIndex]
	for z in range(1, len(bestTour)):
		if str(bestTour[z].id) in idDict:
			print("Duplicate City id found.  Results are invalid.")
			return False
		else:
			idDict[str(bestTour[z].id)] = 1

	# If this return statment is true no duplicate ID's found.
	return True


if __name__ == '__main__':
	print("tspmain.py  has run.")
	cities = importCase()
	# print("main cities")
	# print(cities)
	results = singleThreadedTsp(cities)
	if checkResultShortest(results):
		print("All good in the hood.")