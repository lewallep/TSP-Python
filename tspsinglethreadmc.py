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

	def 

	# The function to call for each individual process.
	# Prereque is to have a range of cities from the list passed to it.
	# Deep copying will happen in the base tour.
	def tourSingle(qr, startCities, cities):
		# print("threadedCities len(): " + str(len(threadCities)))
		results = tspsinglethread.TspSingleThread.singleThreadedTsp(startCities)
		# print("results: %s" % (results))
		for i in range(len(startCities)):
			qr.put(results[i])
			print("put a result into the queue")
		# print("tourSingle() is finished.")

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

		for i in range(numprocs):
			results.append(qr.get())
		
		print(results)
		print(len(results))
		return results