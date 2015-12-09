from Light import Light
import re

regx = re.compile("(\d+)\,(\d+)");

def initMatrix():
    matrix = {}
    for i in range(0,1000):
        for j in range(0,1000):
            matrix[i,j] = Light(False)

    return matrix


def execute(matrix, command):
    fromPoint = regx.findall(command)[0]
    fromPoint = (int(fromPoint[0]), int(fromPoint[1]))

    toPoint = regx.findall(command)[1]
    toPoint = (int(toPoint[0]), int(toPoint[1]))

    for i in range(fromPoint[0], toPoint[0] + 1):
        for j in range(fromPoint[1],toPoint[1] + 1):
            matrix[i,j].runCommand(command)



def getFile():
    return open("advent6.txt", 'r')


def main():
    matrix = initMatrix()
    lit = 0

    for line in getFile():
        execute(matrix, line)

    for x in range(0,1000):
        for y in range(0,1000):
            if(matrix[x,y].state):
                lit += 1


    print("Lights lit: " + str(lit))


if  __name__ =='__main__':main()
#569999
