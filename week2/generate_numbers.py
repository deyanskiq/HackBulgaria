import sys
from random import randint


def main():
    number = int(sys.argv[2])
    f = open(sys.argv[1], "w")
    lst = []
    for item in range(1, number):
        lst.append(randint(1, 1000))
    f.write(",".join(map(str, lst)))
    f.close()

if __name__ == '__main__':
    main()
