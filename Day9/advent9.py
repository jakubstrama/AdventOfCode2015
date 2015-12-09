from RouteModule import Route
import re

def getFile():
    return open("Day9/advent9.txt", 'r')

def createRoute(word):
    reg = re.findall("(\w+)\sto\s(\w+)\s=\s(\d+)", word)
    for fromCity, toCity, distance in reg:
        return Route(fromCity, toCity, distance)

def main():
    routes = []
    for line in getFile():
        route = createRoute(line)
        routes.append(route)
        print(route)




if  __name__ =='__main__':main()
