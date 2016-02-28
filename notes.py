#!/usr/bin/python

print "The xInterval is: " + str(xInterval)
print "The yInterval is: " + str(yInterval)
print

print "rangeX: " + str(rangeX)
print "rangeY: " + str(rangeY)

print
print "sdXRemainder: %d" % (sdXRemainder)
print "sdYRemainder: %d" % (sdYRemainder)
print 

print "sectorDistX " + str(sectorDistX)
print "sectorDistY " + str(sectorDistY)
print

print "Printing sectorExtents"
	
for i in range(0, len(sectorExtents)):
	print "i = " + str(i)
	print
	print "secMinX: " + str(sectorExtents[i].secMinX)
	print "secMaxX: " + str(sectorExtents[i].secMaxX)
	print "secMinY: " + str(sectorExtents[i].secMinY)
	print "secMaxY: " + str(sectorExtents[i].secMaxY)
	print


dist = int(round(math.sqrt((cityTwo[1] - cityOne[1])**2 + (cityTwo[2] - cityOne[2])**2)))




# old single threaded solution. 
# Required tuples and now switching to city objects.
	for startCity in range(0, numCities):
		print  "The startCity is: " + str(startCity)
		citiesNotVisited = copy.deepcopy(cityList)

		curCity = citiesNotVisited[startCity]

		# For simplicity when starting a test tour we will always start at the 
		nextCity = citiesNotVisited[0]
	
		while len(citiesNotVisited) > 0:
			print "citiesNotVisited len: " + str(len(citiesNotVisited))

			while nextCityIndex < len(citiesNotVisited):
				if nextCityIndex != startCity:

					nextCity = citiesNotVisited[nextCityIndex]
					dist = int(round(math.sqrt((nextCity[1] - curCity[1])**2 + (nextCity[2] - curCity[2])**2)))
					print "While 3  nextCityIndex: " + str(nextCityIndex)
					print "dist: " + str(dist)
					
					if dist < distBestSoFar:
						curCity = nextCity
						curTour += dist	
						nextCityIndex += 1
					else:
						print "Inside the else statement"
					
					nextCityIndex += 1

			del citiesNotVisited[len(citiesNotVisited) - 1]

			nextCityIndex = 0

		print



3 913 933
4 632 678