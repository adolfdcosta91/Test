#Dqueue
# Append Left , Append Right
# Pop, Pop Left

import collections


list = ["Sun","Mon","Tues"]

DoubleEnd = collections.deque(list)


def printDqueue(printDqueue):
    for i in range(len(printDqueue)):
        print(printDqueue[i])
    print("\n")

printDqueue(DoubleEnd)



DoubleEnd.append("Wed")
printDqueue(DoubleEnd)

DoubleEnd.appendleft("Thus")
printDqueue(DoubleEnd)


DoubleEnd.pop()
printDqueue(DoubleEnd)

DoubleEnd.popleft()
printDqueue(DoubleEnd)
