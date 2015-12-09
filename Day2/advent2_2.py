import functools

def getBowlength(dimensions):
    return dimensions[0] * dimensions[1] * dimensions[2]

def getRibbonLength(dimensions):
    dimensions.remove(max(dimensions))
    dimensions = list(map(lambda x: x*2, dimensions))
    length = functools.reduce(lambda x, y: x+y, dimensions)

    return length

def getLength(dimensions):
    return getBowlength(dimensions) + getRibbonLength(dimensions)


def getFile():
    return open("advent2.txt", 'r')


def main():
    total = 0

    for line in getFile():
        dimensions  = line.strip().rstrip("\n").split('x')
        dimensions = list(map(int, dimensions))
        total += getLength(dimensions)

    print("total is " + str(total))


if  __name__ =='__main__':main()
#3842356
