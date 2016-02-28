#!/usr/bin/python
import os, math, sys
import classTest

def main(args):
	print "The args of this program are . . ."

	for i in range(0, len(args)):
		print args[i]

	city = []
	city.append(classTest.CityObject(1, 300, 200, 67.54))

	print city[0].index
	print city[0].xCoord
	print city[0].yCoord
	print city[0].distNext

	city.append(classTest.CityObject(2, 400, 200, 0))

	print city[1].index
	print city[1].xCoord
	print city[1].yCoord
	print city[1].distNext

if __name__ == '__main__':
	main(sys.argv)