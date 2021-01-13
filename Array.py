# Array operation in python

from array import *

# arrayName = array(typecode, [Initializers])

TempArray = array('i',[0])


TempArray.insert(1,2)
TempArray.insert(2,5)

print(TempArray[0])
print(TempArray[1])
print(TempArray[2])

print("\n")

#Print an array
for i in range(len(TempArray)):
    print(TempArray[i])