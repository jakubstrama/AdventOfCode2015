#2565
from Santa import Santa

def main():
    file3 = open("advent3.txt", "r")
    houseList = {}
    santa = Santa(houseList)

    for ch in iter(lambda: file3.read(1), ''):
        santa.move(ch)

    print(len(houseList))


if __name__ == "__main__": main()
