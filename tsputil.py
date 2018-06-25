# Provides classes and funtionality for testing the results of the TSP answers.
# Provides functionality for inputting the cities from the chosen test case.
from collections import namedtuple
import sys

City = namedtuple("City", ["id", "x", "y"])

class TspUtil:
	# import the cities from the text file
	# Returns a list of cities.  Cities = named tuple?
	def importCase():
		cities = []

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

	# Finds the shortest tour overall from the dictionary of results.
	# Does not recompute the tour.  Simply reads and stores the shortest tour index
	# from the dict.
	def findShortestTourOverall(results):
		shortest = sys.maxsize
		shortestTour = []
		for i in range(len(results)):
			print("%s" % (results[i][0]))
			if results[i][0] < shortest:
				shortest = results[i][0]
				shortestTour = results[i]

		print("shortestTour: ")
		print("shortest: %s" % (shortest))
		print(shortestTour)
				