HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def printError(str):
    print(FAIL + BOLD + "NON! " + str + ENDC)

def printSuccess(str):
    print(OKGREEN + "OK! Le test est passé pour " + str + ENDC)

def test_e1a(e1a):
    values = [[0, True], [20, False], [19, True], [-1, False]]
    for value in values :
        if e1a(value[0]) != value[1]: 
            printError(str(value[0]) + " devrait retourner " + str(value[1]))
        else:
            printSuccess(str(value[0]))

def test_e1b(e1b):
    values = [["a","a", False], ["a","B", False], ["a","A", True], ["A","a", True], ["A","A", False]]
    for value in values :
        if e1b(value[0], value[1]) != value[2]: 
            printError(str(value[0]) + " et " + str(value[1]) + " devrait retourner " + str(value[2]))
        else:
            printSuccess(str(value[0]) + " et " + str(value[1]))

def test_e1c(e1c):
    values = [[2, 2, True], [2, 6, False], [0, 0, False], [1, 16, True]]
    for value in values :
        if e1c(value[0], value[1]) != value[2]: 
            printError(str(value[0]) + " et " + str(value[1]) + " devrait retourner " + str(value[2]))
        else:
            printSuccess(str(value[0]) + " et " + str(value[1]))

def test_e1d(e1d):
    values = [["ajfklds", False], ["Ajfkld", True], ["Mjfkld", False], ["Ajfkl", False], ["Ajfkldf", False]]
    for value in values :
        if e1d(value[0]) != value[1]: 
            printError(str(value[0]) + " devrait retourner " + str(value[1]))
        else:
            printSuccess(str(value[0]))

def test_int_sqrt(int_sqrt):
    values = [[8, 2], [7, 2], [17, 4], [25, 5], [90, 9]]
    for value in values :
        if int_sqrt(value[0]) != value[1]: 
            printError(str(value[0]) + " devrait retourner " + str(value[1]))
        else:
            printSuccess(str(value[0]) + " valeur de retour " + str(value[1]))

def my_init_square(a):
    x = 0
    while x*x <= a:
        x = x + 1 
    return x - 1

def next_heron_sqrt(un, a):
    return (un + (a/un))/2

def test_heron_sqrt(heron_sqrt, a, n):
    myVal = my_init_square(a)
    # print("u0:" + str(myVal))
    for i in range(1, n+1):
        myVal = next_heron_sqrt(myVal, a)
        # print("u"+ str(i) + ":" + str(myVal))

    # print(str(myVal*myVal))
    if myVal != heron_sqrt(a, n):
        printError("heron_sqrt devrait retourner " + str(myVal) + ", valeur obtenue " + str(heron_sqrt(a, n)))
    else:
        printSuccess("")

def test_heron_rank(heron_rank, a, p):
    n = 0
    myVal = my_init_square(a)
    while abs((myVal*myVal) - a) > p:
        myVal = next_heron_sqrt(myVal, a)
        n = n + 1
    rank = heron_rank(a, p)
    if n != rank:
        printError("heron_rank devrait retourner " + str(n) + ", valeur obtenue " + str(rank))
    else:
        printSuccess("")
    