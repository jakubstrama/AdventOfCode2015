import hashlib, re

#4.1 starts with 5 zeros  - 282749
pattern = re.compile('[0]{5,}\w+')

#4.2 starts with 6 zeros - 9962624
pattern = re.compile('[0]{6,}\w+')


def getHash(key, num):
    inputStr = key + str(num)
    m = hashlib.md5()
    m.update(str.encode(inputStr))
    return m.hexdigest()

def checkHash(hash):
    global pattern
    return bool(pattern.match(hash))

def main():
    for num in range(0,10000000):
        hashed = getHash("yzbqklnj", num)
        if(checkHash(hashed)):
            print(hashed)
            print(num)
            break




if  __name__ =='__main__':main()
