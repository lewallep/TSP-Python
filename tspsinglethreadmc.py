# Imports the cities from a tab separated text file.
import sys
import tspsinglethread
import multiprocessing

# Start a different thread for each cpu.
# Use queues for communication to each individual thread out to the parent thread.
# Pass in the split list to each calling function.


class TspSingleThreadMc:
	# Count the amaount of available cpus.
	numprocs = multiprocessing.cpu_count()

	# The function to call for each individual process.
	# Prereque is to have a range of cities from the list passed to it.
	# Deep copying will happen in the base tour.
	def tourSingle(threadCities):	

	def tourmc(numprocs, cities):
		qr = Queue()	#Results from the different processes
		p = Process()