
def getArea(l,w,h):
    area = (2*l*w) + (2*w*h) + (2*h*l)
    area += getSmallestSide(l,w,h)
    return area

def getSmallestSide(l,w,h):
    smallest = []
    smallest.append(l*w)
    smallest.append(w*h)
    smallest.append(h*l)

    return min(smallest)


def getFile():
    return open("advent2.txt", 'r')


def main():
    total = 0

    for line in getFile():
        dimensions  = line.strip().rstrip("\n").split('x')
        dimensions = list(map(int, dimensions))
        total += getArea(dimensions[0], dimensions[1], dimensions[2])

    print("total is " + str(total))


if  __name__ =='__main__':main()
