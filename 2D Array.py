# 2 Dimetional Array

# THIS FILE IS EDITED

# Two dimensional array is an array within an array. It is an array of arrays. In this type of array the position of
# an data element is referred by two indices instead of one. So it represents a table with rows an dcolumns of data.
# In the below example of a two dimensional array, observer that each array element itself is also an array.

from array import *

arr2D = [[1,2,3],[10,5,6],[4,5,0]]

for i in range(len(arr2D)):       # Prints all the values
    print (arr2D[i])

print("\n")
# Tio print specific elements from multidimetional array


print(arr2D[0])        # It will print the zero array
print("\n")
print(arr2D[1][2])     # Will select the first array and them the second element from it

