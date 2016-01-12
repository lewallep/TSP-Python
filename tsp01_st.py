#!/usr/bin/python
import sys, math, re, time, copy

# This group of classes encapsulates my distance finding algorithm
# for a single threaded environment.  

def singleThreadedTour(object):
    #Iterate through each city to test all of the possible combinations in the sector.
    #Keep the shortest path for each sector.
    sectorTourLength = 0
    sectorTour = []
    tourStart = 0       

    dist = sys.maxint
    distNext = sys.maxint
    bestSoFar = sys.maxint
    nextCityIndex = -1
    curCityIndex = -1

    curCity = object[1]
    nextCity = object[2]

    # curTour is the tour for each starting city possiblity.
    curTour = []
    tempBest = curCity
    cityVisitedIndex = -1

    tourDist = 0        # The current tour distance.
    bestTourDist = sys.maxint   # The best sector tour distance.

    # Index marker which always starts at the beginning of the list and works though all of the elements
    # Starting at index 1 skips the identifier for the thread at the beginning of the data structure
    nextIterator = 0

    print "tourDist before while loops: " + str(tourDist)
    print "num cities: " + str(len(object))
    print "object: "
    print str(object)
    print


    while tourStart < len(object):
        sectorNotVisited = copy.deepcopy(object)
        curCityIndex = tourStart
        curCity = object[curCityIndex]
        curTour.append(curCity)

        while len(sectorNotVisited) > 0:
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
                # print "distNext: " + str(distNext)
                tourDist += distNext
                # Resetting the temporary distances for tour.
                dist = sys.maxint
                distNext = sys.maxint
                # print "tourDist: " + str(tourDist)

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
    print str(sectorTour)
	    