import re, json

def getFile():
    return open("Day8/advent8.txt", 'r')


def calculateStrippedLength(word):
    simple = len(word)
    stripped = len(eval(word))
    return simple - stripped -1

def calculateEncodedLength(word):
    encoded = len(json.dumps(word))
    simple = len(word)
    return encoded - simple -1

def main():
    total1 = 0
    total2 = 0

    for line in getFile():
        total1 += calculateStrippedLength(line)
        total2 += calculateEncodedLength(line)

    print(total1)
    print(total2)


if  __name__ =='__main__':main()
#1371
#2117
