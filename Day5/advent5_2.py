
def checkOverlaps(word):
    for i in range(0, len(word)):
        twoLetters = word[i:i+2]
        if(word.count(twoLetters) > 1):
            return True

    return False


def checkDoubles(word):
    for i in range(0, len(word)):
        sliced = word[i:i+3]
        if(len(sliced) > 2 and (sliced[0] == sliced[2])):
            return True

    return False


def getFile():
    return open("advent5.txt", 'r')


def main():
    total = 0

    for line in getFile():
        if(checkOverlaps(line) and checkDoubles(line)):
            total +=1

    print("total is " + str(total))


if  __name__ =='__main__':main()
