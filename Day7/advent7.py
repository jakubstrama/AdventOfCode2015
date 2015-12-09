import re
from OperationModule import Operation

def initOperation(collection, operations, command):

    inst = re.findall("([a-zA-Z0-9]*)\s(AND|OR|LSHIFT|RSHIFT)\s([a-zA-Z0-9]*)\s\-\>\s([a-zA-Z0-9]*)", command)
    notInst = re.findall("(NOT)\s([a-zA-Z0-9]*)\s\-\>\s([a-zA-Z0-9]*)", command)
    assignInst = re.findall("^([a-zA-Z0-9]*)\s\-\>\s([a-zA-Z0-9]*)", command)

    if(bool(inst)):
        for left, operator, right, target in inst:
            operations.append(Operation(collection, left, right, target, operator))

    if(bool(notInst)):
        for operator, left, target in notInst:
            operations.append(Operation(collection, left, None, target, operator))

    if(bool(assignInst)):
        for left, target in assignInst:
            operations.append(Operation(collection, left, None, target, "ASSIGN"))


def initOperations(collection, operations):
    for line in getFile():
        initOperation(collection, operations, line)


def getFile():
    return open("advent7.txt", 'r')


def main():
    collection = {}
    operations = []
    done = 0

    initOperations(collection, operations)

    while(len(operations) > done):
        for op in operations:
            if(op.isReady()):
                op.runCommand()
                done += 1

    print(collection["a"])

    ##############
    # Advent 7_2 #
    ##############

    # Assign output of 'a' to 'b' in source file - line nr. 55

if  __name__ =='__main__':main()
#1 - 16076 oldB =19138
#2 - 2797 newB = 16076
