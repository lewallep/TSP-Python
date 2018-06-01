import os, sys, copy
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
	print("inside tour. . . . . . . . . . .  ..")
	print(cities)
	localCities = copy.deepcopy(cities)
	tour = []
	distance = sys.maxsize
	print("len(City): %s" % (len(localCities)))
	print("startCity: " + str(startCity))

	curCity = localCities[startCity]
	localCities.pop(startCity) 
	# print(curCity)
	# print(cities)
	tour.append(curCity)

	while len(localCities) > 0:
		# Find next closest city
		print("localCities length: %s" % len(localCities))
		tour.append(localCities[0])
		localCities.pop(0)

	# print(tour)
	return distance, tour


# Processes the results in real time.
# Each iteration update the lowest overall tour length.

# wrapper loop that takes iterates over the import cases and passes in the start ID
# Returns a list with all of the tours and shortest tour.
def singleThreadedTsp(cities):
	print("singleThreadedTsp()")
	# print(cities)
	shortestDist = sys.maxsize
	curDistance = sys.maxsize
	curTour = []
	shortestTour = []
	results = []

	#print(shortestTour)
	for i in range(len(cities)):
		curDistance, curTour = tour(cities, i)
		curTour.insert(0, curDistance)
		results.append(curTour)
		if curDistance < shortestDist:
			shortestDist = curDistance
			shortestTour = curTour

if __name__ == '__main__':
	print("tspmain.py  has run.")
	cities = importCase()
	# print("main cities")
	# print(cities)
	singleThreadedTsp(cities)