#!/usr/bin/python
import os, math, sys

class CityObject:
	def __init__(self, index, xCoord, yCoord, distNext):
		self.index = index
		self.xCoord = xCoord
		self.yCoord = yCoord
		self.distNext = distNext