from sys import argv


def sum_integers():
    lst = []
    f = open(argv[1], "r")
    for line in f:
        for word in line.split():
            if word == int(word):
                lst.append(int(word))
    print (sum(lst))
sum_integers()
