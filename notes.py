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