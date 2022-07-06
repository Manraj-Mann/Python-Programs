# empty friends 

from lib2to3.pgen2 import driver

from attr import field
from more_itertools import first


friends = []

# pritn empty 

print( friends)

# adding elementts 

friends = ["Name" , "ejllo"]

print(friends)

# insertion at last 

friends.insert(len(friends), 23)

print(friends)

print(friends[0])

#range 

print(friends[0:2])

print(friends[1 : ])
print(friends[ : 2 ])

# modify 

friends[2] = "eh"

print(friends)


enemy = ["ehll" , "hell"]

friends.extend(enemy)
print(friends)

friends.append("Creee")
print(friends)

friends.pop()
print(friends)

friends.insert(round(len(friends)/2) , "Mid")
print(friends)

friends.remove("eh")
print(friends)

friends.insert( len(friends) , "0")

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends2 = friends.copy()

friends.clear()
print(friends)