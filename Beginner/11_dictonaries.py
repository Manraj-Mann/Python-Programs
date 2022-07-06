#  dictonary - key value pair

from setuptools import sic


dict = { }

#empty dict

print(dict)

dict = {

    #key : value

    1 : "Manraj",
    2: "Someone",
    3: "Someone else"
}

print(dict)
print(dict[1])

print(dict.get(10 , "Not found"))