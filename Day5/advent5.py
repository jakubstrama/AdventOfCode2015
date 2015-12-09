import re

vowels = {"a", "e", "i", "o", "u"};
patternDouble = re.compile("([a-z])\\1{1,}");
excludes = {"ab", "cd", "pq", "xy"};


def checkVowels(word):
    vtotal = 0
    for chr in word:
        if(chr in vowels):
            vtotal +=1

    return vtotal > 2


def checkDoubles(word):
    return bool(patternDouble.search(word))


def checkExcludes(word):
    for exclude in excludes:
        if(exclude in word):
            return False

    return True


def getFile():
    return open("advent5.txt", 'r')


def main():
    total = 0

    for line in getFile():
        if(checkVowels(line) and checkDoubles(line) and checkExcludes(line)):
            print(line)
            total +=1

    print("total is " + str(total))


if  __name__ =='__main__':main()
