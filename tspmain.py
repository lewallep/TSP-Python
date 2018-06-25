import os, sys, copy, math
from collections import namedtuple
from tspsinglethread import TspSingleThread 
import tsputil, tspsinglethreadmc


# Takes a tour and it's distance and checks to see if any of the edges 
# intersect each other.
# Only checks a subset of 4 connected vertexes at a time.
# Ideally this would be connected to the tours to identify and unwind intersections
# as the nearest neighbors are found.

if __name__ == '__main__':
	tspu = tsputil.TspUtil
	cities = tspu.importCase()
	# print("main cities")
	# print(cities)
	if sys.argv[2] == "st":
		tsp = TspSingleThread
		results = tsp.singleThreadedTsp(cities)
	elif sys.argv[2] == "mc":
		print("Inside the mc argument")
		tspmc = tspsinglethreadmc.TspSingleThreadMc
		results = tspmc.tourmc(cities)

	if tspu.checkResultShortest(results):
	 	tspu.findShortestTourOverall(results)