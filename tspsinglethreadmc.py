# Imports the cities from a tab separated text file.
import sys
import tspsinglethread
import multiprocessing
from multiprocessing import Queue, Process
import math

# Start a different thread for each cpu.
# Use queues for communication to each individual thread out to the parent thread.
# Pass in the split list to each calling function.
class TspSingleThreadMc:
	# Count the amaount of available cpus.
	numprocs = multiprocessing.cpu_count()

	# A copy of the singleThreadedTsp(cities) function but takes the start cities list as
	# an argument along with the cities list.  
	def singleThreadedMc(startCities, cities):
		shortestDist = sys.maxsize
		curDistance = sys.maxsize
		curTour = []
		shortestTour = []
		results = []
		
		for i in range(len(startCities)):
			curStartCity = startCities[i].id
			# print("startCities[i].id: %s" % (curStartCity))
			curDistance, curTour = tspsinglethread.TspSingleThread.tour(cities, curStartCity)
			curTour.insert(0, curDistance)
			results.append(curTour)
			print("i: %s 	curTour: %s" % (i, curTour[0]))
			if curDistance < shortestDist:
				shortestDist = curDistance
				shortestTour = curTour

		return results


	# The function to call for each individual process.
	# Prereque is to have a range of cities from the list passed to it.
	# Deep copying will happen in the base tour.
	def tourSingle(qr, startCities, cities):
		# print("threadedCities len(): " + str(len(threadCities)))
		results = TspSingleThreadMc.singleThreadedMc(startCities, cities)
		# print("tourSingle results length: %s" % (len(results)))
		for i in range(len(startCities)):
			# print("inside a single core results: " + str(results[i][0]))
			qr.put(results[i])
		print("tourSingle() is finished.")

	# Divides up the cities into different lists for each processor to have as close to an event amount as possible.
	# Each list can only accept integers as arguments to the begining and end of the list.
	# def divideCities():
	def tourmc(cities):
		numprocs = TspSingleThreadMc.numprocs
		qr = Queue()	#Results from the different processes
		numCities = len(cities)
		# threadCities = cities[:math.floor(len(cities)/numprocs)]
		results = []
		citiesPerProc = math.floor(numCities / numprocs)
		# print("citiesPerProc: " + str(citiesPerProc))
		citiesRemainder = numCities % numprocs
		# print("citiesRemainder: " + str(citiesRemainder))		

		# Initializing index aId and bId representing the start and end each processes city id's.
		aId = 0
		bId = 0
		
		for i in range(0, numprocs):
			if citiesRemainder > 0:
 				bId = bId + 1 + citiesPerProc	#Increments the 
 				citiesRemainder -= 1
			else:
				bId = aId + citiesPerProc

			# print("i: %s aId %s bId: %s" % (i, aId, bId))
			p = Process(target=TspSingleThreadMc.tourSingle, args=(qr, cities[aId:bId], cities))
			p.start()
			# print("citiesRemainder: " + str(citiesRemainder))
			aId = bId	#Incrementing the start of the next list slice.

		for i in range(numCities):
			results.append(qr.get())
		
		# print(results)
		# print(len(results))
		for i in range(numprocs):
			p.join()

		qr.close()
		return results
		# ssh enabled.  It is like shake and bake with Ricky bobby but not.
		# All of this should be refactored to instantiated objects instead of the singular class I have now.  
		# This might also help with the pickling issue of the named tuple.