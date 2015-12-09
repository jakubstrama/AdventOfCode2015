#2639
from Santa import Santa

def main():
    file3 = open("advent3.txt", "r")
    houseList = {}

    santa = Santa(houseList)
    roboSanta = Santa(houseList)

    for ch in iter(lambda: file3.read(2), ''):
        santa.move(ch[0])
        if(len(ch) > 1):
            roboSanta.move(ch[1])

    print(len(houseList))


if __name__ == "__main__": main()
