# Generates .txt files of cities with an id and x and y coordinates.
# X and Y coordinates are generated from the specified range.
# Ouput path will be to a local folder unless otherwise specified on the command line.
import sys, random, os
from collections import namedtuple

#Gets the command line args and returns a dictioanry.
def argsDict():
    commArgs = {}
    # print("num args: " + str(len(sys.argv)))

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "numcities":
            commArgs["numcities"] = int(sys.argv[i+1])
            i += 1
        elif sys.argv[i] == "xmax":
            commArgs["xmax"] = int(sys.argv[i+1])
            i += 1
        elif sys.argv[i] == "ymax":
            commArgs["ymax"] = int(sys.argv[i+1])
            i += 1
        elif sys.argv[i] == "location":
            commArgs["location"] = sys.argv[i+1]
            i += 1

    return commArgs

# Does some stuff.
# Takes the dictionary of arguments and creates the file in the location specified.
# If no location specified creates a folder called "testcases" in the local folder
# where the script is run.
# Writes out the file with a streaming buffer.
# Write the number of cities as a suffix on the filename.
def makeFile(myArgs):
    random.seed()
    if "location" in myArgs:
        print(myArgs["location"])
        with open(myArgs["location"], 'r+') as f:
            for i in range(myArgs["numcities"]):
                f.write(str(random.randint(0, myArgs["xmax"])))
        f.close()
    else:
        if not os.path.exists("testcases"):
            os.makedirs("testcases")
        with open("testcases/cities" + str(myArgs["numcities"]) + ".txt", 'r+') as f:
            f.write(str(myArgs["numcities"]) + "\t" + str(myArgs["xmax"]) + "\t" + \
                str(myArgs["ymax"]) + "\n")
            for i in range(myArgs["numcities"]):
                f.write(str(i) + "\t")
                f.write(str(random.randint(0, myArgs["xmax"])))
                f.write("\t" + str(random.randint(0, myArgs["ymax"])) + "\n")
            _fixDuplicateCities(f, myArgs)
        f.close()

# Iterates over the cities in the text file and finds any with duplicate x and y values.
# If there are duplicate valules, it first looks to inrement or decrement the x value by 1.
# If the city is bracketed it tries to find the next closest y value.
# This is only called by the makeFile(myArgs) function.
# It makes a map of the values meaning the memory usage can be high.
def _fixDuplicateCities(f, args):
    f.seek(0)   # using the same file descriptor settings and going back to the start of file.
    firstLine = f.readline()    # Instead of seeking to the next line I just grab and not use
    cities = {}
    City = namedtuple("City", ["x", "y"]) # the value of the map element is the city id

    for i in range(args["numcities"]):
        startLine = f.tell()
        line = f.readline().strip()
        endLine = f.tell()
        tokens = line.split("\t")
        c = City(x = tokens[1], y = tokens[2])
        if c in cities:
            print("Found a duplicate x y coordinates: " + str(c))

        else:
            cities[c] = tokens[0]   # Add a City named tuple element with the id for the map elem value.

    print("len(cities): " + str(len(cities)))
    print("cities: ")
    for city in cities.items():
        print(city)


    # making a test commit.
    # another test commit.

    # Practice incrementing a single named tuple.
    # c = City(x = 100, y = 200)
    # cities[c] = 1
    # if City(x = 100, y = 200) in cities:
    #     cx = c.x
    #     cy = c.y + 1
    #     print(cx)
    #     print(cy)

    #     cIncremented = City(x = cx, y = cy)
    #     print(cIncremented)

    
    # Deprecating as this removed specific cities.
    # for i in range(args["numcities"]):
    #     line = f.readline().strip() 
    #     tokens = line.split("\t")
    #     if tokens[1] not in cities:
    #         cities[tokens[1]] = tokens[2]   #If the x coor is not held place the y value.
    #     else:   # A duplicate x value has been detected.  Analyzing the y value.
    #         if cities[tokens[1]] == tokens[2]:
    #             print("We also have a duplicate y value. Incrementing one value.")
    #             yval = int(tokens[2])
    #             yval += 1
    #             tokens[2] = str(yval)
    #             print("tokens after incrementing y: " + str(tokens))

if __name__ == '__main__':
    print("Generating cities.")
    testArgs = argsDict()
    makeFile(testArgs)