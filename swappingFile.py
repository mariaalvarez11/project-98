def swapFileData():
    f1 = input("enter file name:- ")
    f2 = input("enter file name:- ")


    with open(f1, 'r') as a:
    dataA = a.read()

    with open(f2, 'r') as b:
    dataB = b.read()

    with open(f1, 'w') as a:
    a.write(dataB)

    with open(f2, 'w') as b:
    b.write(dataA)

swapFileData()