#!/usr/bin/python
import sys, math, re, time
import multiprocessing as mp
import thread

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

def distributeCities(fullCityList, minMax):
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

	print "The xInterval is: " + str(xInterval)
	print "The yInterval is: " + str(yInterval)

	rangeX = minMax.maxX - minMax.minX
	rangeY = minMax.maxY - minMax.minY
	print "rangeX: " + str(rangeX)
	print "rangeY: " + str(rangeY)

	sectorDistX = rangeX / xInterval
	sectorDistY = rangeY / yInterval

	sdXRemainder = rangeX % xInterval
	sdYRemainder = rangeY % yInterval

	print
	print "sdXRemainder: %d" % (sdXRemainder)
	print "sdYRemainder: %d" % (sdYRemainder)
	print 

	sectorExtents = []
	
	for x in range(0, xInterval):
		for y in range(0, yInterval):
			print "Inner for loop"
			#curSector.append(minMax.minX)
			#curSector.append((x * sectorDistX) + sectorDistX + minMax.minX)
			#curSector.append(minMax.minY)
			#curSector.append((y * sectorDistY) + sectorDistY + minMax.minY)
			#print "curSector minX: %d, maxX: %d, minY: %d, maxY: %d" % (curSector[0], curSector[1], curSector[2], curSector[3])


	sectorExtents.append(curSector(5, 6, 7, 8))

	print 
	print "The sector extents are: " + str(sectorExtents[0].secMinX) + str(sectorExtents[0].secMaxX)
	print

	print
	print "sectorDistx " + str(sectorDistX)
	print "sectorDisty " + str(sectorDistY)
	print

	return numProcs

def main(args):
	#Introduction message.
	print "I have run my main function.  Wow. . . "
	print

	fullCityList = importCities(args[1])

	numCities = len(fullCityList)
	print "The number of cities is is " + str(numCities)

	for city in fullCityList:
		print str(city[0]) + "\t" + str(city[1]) + "\t" + str(city[2])

	overallMinMax = findExtents(fullCityList)

	print
	print "MIN X : " + str(overallMinMax.minX)
	print "MAX X : " + str(overallMinMax.maxX)
	print
	print "MIN Y : " + str(overallMinMax.minY)
	print "MAX Y : " + str(overallMinMax.maxY)
	print

	cityDistributed = distributeCities(fullCityList, overallMinMax)

	#Print the final parting message
	print
	print "End of Line.  I oh so love Aliens."

if __name__ == '__main__':
	main(sys.argv)