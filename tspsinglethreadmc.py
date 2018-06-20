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

	# The function to call for each individual process.
	# Prereque is to have a range of cities from the list passed to it.
	# Deep copying will happen in the base tour.
	def tourSingle(qr, threadCities):
		print("tourSingle()")
		print("threadedCities len(): " + str(len(threadCities)))

	def tourmc(cities):
		numprocs = TspSingleThreadMc.numprocs
		qr = Queue()	#Results from the different processes
		numCities = len(cities)
		threadCities = cities[:math.floor(len(cities)/numprocs)]
		
		print("cities length: " + str(len(cities)))
		for i in range(0, numprocs):
			print("This is where I will need to put the process.stat()")
			p = Process(target=TspSingleThreadMc.tourSingle, args=(qr, threadCities))
			p.start()

		for i in range(0, numprocs):
			p.join()