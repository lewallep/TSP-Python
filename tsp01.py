#!/usr/bin/python
import sys, math, re, time, os
import multiprocessing as mp
import thread
import tsp01_tp

class minMax(object):
	def __init__(points, minX, maxX, minY, maxY, numCities):
		points.minX = minX
		points.maxX = maxX
		points.minY = minY
		points.maxY = maxY
		points.numCities = numCities

class curSector(object):
	def __init__(sector, secMinX, secMaxX, secMinY, secMaxY):
		sector.secMinX = secMinX
		sector.secMaxX = secMaxX
		sector.secMinY = secMinY
		sector.secMaxY = secMaxY

def importCities(fname):
	inputFile = open(fname)
	cityList = []
	for line in inputFile:
		record = line.split()
		city = (int(record[0]), int(record[1]), int(record[2]))
		cityList.append(city)

	return cityList

# findExtents
# Prereqruisites: there has to be a list of cities with x and y coordinates.
# Output: Returns single class object of minMax to the calling function.
def findExtents(fullCityList):

	minX = 9999999
	maxX = 0
	minY = 9999999
	maxY = 0
	numCities = len(fullCityList)

	for city in fullCityList:
		currentX = city[1]
		currentY = city[2]
		if currentX < minX:
			minX = currentX
		if currentX > maxX:
			maxX = currentX
		if currentY < minY:
			minY = currentY
		if currentY > maxY:
			maxY = currentY

	extents = minMax(minX, maxX, minY, maxY, numCities)

	return extents

# defineSectors
# Prerequrisites the minMax class has been defined with the overall range of city coordinates
# for the list of cities.
# Output: Returns a list of sectors based on the number of processors.
def defineSectors(minMax):
	# This function will calculate the number of available processors and stuff
	# it into a 2D list to pass around to other functions.
	numProcs = mp.cpu_count()
	print "The processor count is: " + str(numProcs)

	divisor = 2

	xInterval = numProcs / divisor
	yInterval = numProcs / xInterval

	while xInterval > (divisor * 2):
		divisor += 1

	if (divisor * divisor) == numProcs:
		xInterval = numProcs / divisor
		yInterval = numProcs / divisor
	else:
		xInterval = numProcs / divisor
		yInterval = divisor

	rangeX = minMax.maxX - minMax.minX
	rangeY = minMax.maxY - minMax.minY

	sectorDistX = rangeX / xInterval
	sectorDistY = rangeY / yInterval

	sdXRemainder = rangeX % xInterval
	sdYRemainder = rangeY % yInterval

	# Declare Sector Extents.
	sectorExtents = []

	# Local variables to work with before adding them to the sector extents list.
	localMinX = 0
	localMaxX = 0
	localMinY = 0
	localMaxY = 0

	for i in range(0, xInterval):
		# Now calculate the X coordinate sector values
		localMinX = (i * sectorDistX) + minMax.minX
		localMaxX = localMinX + sectorDistX
		#Calculate the Y values for the sector.
		for z in range(0, yInterval):
			localMinY = (z * sectorDistY) + minMax.minY
			localMaxY = localMinY + sectorDistY
			if (z == (yInterval - 1)):
				localMaxY += sdYRemainder
			sectorExtents.append(curSector(localMinX, localMaxX, localMinY, localMaxY))
		# Reset the values for the next sector
		localMaxY = 0

	return sectorExtents

def organizeCitiesBySector(citySectors, fullCityList):
	print "I am in the called function in a process."
	print "process id inside organizeCitiesBySector " + str(os.getpid())
	print

	tsp01_tp.printCities(fullCityList)

	return "organizeCitiesBySector has returned."

def organizeCities(citySectors, fullCityList):
	p = mp.Process(target = organizeCitiesBySector, args = (citySectors, fullCityList,))
	p.start()
	p.join()

	return "Super organized.  Oh yeeeea!"

def main(args):
	#Introduction message.
	print "I have run my main function.  Wow. . . "
	print

	fullCityList = importCities(args[1])

	numCities = len(fullCityList)
	print "The number of cities is is " + str(numCities)

	# test print to ensure all of the cities were imported in the proper format.
	# tsp01_tp.printCities(fullCityList)

	#Find the overall extents of the city list.
	overallMinMax = findExtents(fullCityList)

	# Define the 
	citySectors = defineSectors(overallMinMax)

	## testing classes
	# tsp01_tp.printSectors(citiesDistributed)
    # tsp01_tp.printExtents(overallMinMax)

	citiesSectorOrganized = organizeCities(citySectors, fullCityList)

	#Print the final parting message
	print
	print "End of Line.  I oh so love Aliens."

if __name__ == '__main__':
	main(sys.argv)