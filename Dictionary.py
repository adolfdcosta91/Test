# Dictionary in python

# In Dictionary each key is separated from its value by a colon (:), the items are separated by commas, and the whole
# thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces,
# like this: {}.

#Initilize a Dictionary

dict = {'Name':['Adolf','Dcosta'],'Age':['29'],'Sex':['Male']}

print (dict['Name'])
print (dict['Age'])
print (dict['Sex'])
print("\n")

# Overwriting the Dictionary "Name" Key with another name.

print ("Over Writing")
dict['Name'] = 'Zubin'

print (dict['Name'])
print (dict['Age'])
print (dict['Sex'])


# Print key with corresponding value
for key,value in dict.items():
    print("Key: {} - Value:{}".format(key, value))
