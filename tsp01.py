#!/usr/bin/python
import sys, math, re, time, os, copy
import multiprocessing as mp
import tsp01_tp
import tsp01_st
from multiprocessing import Process, Queue

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

# Returns a 2D list of cities.  Each city has an ID number, X coordination, Y coordinate
# Prereqruisite: The list of cities must come from a file with one city
# on each line separated by a '\n' character.
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
    print("The processor count is: " + str(numProcs))

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

def sortCitiesInSector(citiesLocalSector):
    #Iterate through each city to test all of the possible combinations in the sector.
    #Keep the shortest path for each sector.
    sectorTourLength = 0
    sectorTour = []
    tourStart = 1       #Using one to correlate with the indexes of each city. Incremented until 

    dist = sys.maxint
    distNext = sys.maxint
    bestSoFar = sys.maxint
    nextCityIndex = -1
    curCityIndex = -1

    curCity = citiesLocalSector[1]
    nextCity = citiesLocalSector[2]

    # curTour is the tour for each starting city possiblity.
    curTour = []
    tempBest = curCity
    cityVisitedIndex = -1

    tourDist = 0        # The current tour distance.
    bestTourDist = sys.maxint   # The best sector tour distance.

    # Index marker which always starts at the beginning of the list and works though all of the elements
    # Starting at index 1 skips the identifier for the thread at the beginning of the data structure
    nextIterator = 1

#   print "citiesLocalSector: " + str(citiesLocalSector)
#   print "citiesLocalSector Length: " + str(len(citiesLocalSector))

    while tourStart < len(citiesLocalSector):
#       print "tourStart: " + str(tourStart)
        sectorNotVisited = copy.deepcopy(citiesLocalSector)
        curCityIndex = tourStart
        curCity = citiesLocalSector[curCityIndex]
        curTour.append(curCity)

        while len(sectorNotVisited) != 1:
            # While loop through the remaining cities to determin the closest.
            nextCityIndex = 1
            
            while nextCityIndex < len(sectorNotVisited):    
                if curCityIndex != nextCityIndex:
                    nextCity = sectorNotVisited[nextCityIndex]
                    dist = int(round(math.sqrt((nextCity[1] - curCity[1])**2 + (nextCity[2] - curCity[2])**2)))

                    if dist < distNext:
                        distNext = dist
                        tempBest = sectorNotVisited[nextCityIndex]
                        cityVistedIndex = nextCityIndex

                nextCityIndex += 1

                # Appending the current city distance
                tourDist += distNext

                # Resetting the temporary distances for tour.
                dist = sys.maxint
                distNext = sys.maxint

            # Save the closest neighbor
            curTour.append(tempBest)
            # Deleting the city visited to remove from the list for the next closest neighbor selection.
            del sectorNotVisited[cityVisitedIndex]

        if tourDist < bestTourDist:
            bestTourDist = tourDist

        tourDist = 0
        sectorTour = copy.deepcopy(curTour)
        curTour = []
        tourStart += 1
    # End of outermost while loop.

    # This is a placeholder until I finish the logic.
    return sectorTour

def organizeCitiesBySector(citySectors, fullCityList, q, curSector):
    # Declare the container to hold the cities for the designed sector
    citiesLocalSector = []
    # Appending an integer label to identify which sector the cities belong to.
    citiesLocalSector.append(curSector)

    # Move the Cities to one sector
    for i in range(0, len(fullCityList)):
        if citySectors[curSector].secMinX <= fullCityList[i][1] and \
                citySectors[curSector].secMaxX >= fullCityList[i][1] and \
                citySectors[curSector].secMinY <= fullCityList[i][2] and \
                citySectors[curSector].secMaxY >= fullCityList[i][2]:
            # If a city is found to be within the sector append to the list for this sector.
            citiesLocalSector.append(fullCityList[i])
        
    citiesLocalSorted = sortCitiesInSector(citiesLocalSector)

    # Use a queue to transfer this list to the calling process.
    q.put(citiesLocalSorted)


def organizeCities(citySectors, fullCityList, sectorCount):
    # Declare an empty list to hold the processes as they get created.
    allCitiesSectors = []
    q = Queue()

    for i in range(0, sectorCount): 
        curSector = i
        p = Process(target = organizeCitiesBySector, args = (citySectors, fullCityList, q, curSector, ))
        p.start()

    for i in range(0, sectorCount):
        allCitiesSectors.append(q.get())

    for i in range(1, sectorCount):
        p.join()

    for i in range(0, sectorCount):
        print(allCitiesSectors[i])

    return "Super organized.  Oh yeeeea!"

def main(args):
    #Introduction message.
    print("I have run my main function.  Wow. . . ")
    print()

    # For v1.0 the sector count will always equal the cpu count.
    sectorCount = mp.cpu_count()

    fullCityList = importCities(args[1])

    numCities = len(fullCityList)
    print("The number of cities is is " + str(numCities))

    if numCities < 51:
        print("The number of cities was less than 50.") 
        print("Printing the number of cities and exiting.")
        print() 
        print("This explanation is going to be replaced with a single threaded")
        print("functionality for testing purpouses to ensure my tour distance and")
        print("tour path is functional in a single threaded environment.")
        print()

        tsp01_st.singleThreadedTour(fullCityList)
        print() 
    else:
        #Find the overall extents of the city list.
        overallMinMax = findExtents(fullCityList)

        # Define the 
        citySectors = defineSectors(overallMinMax)

        citiesSectorOrganized = organizeCities(citySectors, fullCityList, sectorCount)

        #Print the final parting message
        print()
        print("End of Line.  I oh so love Aliens.")
        print()
        print()
        print()

if __name__ == '__main__':
    main(sys.argv)