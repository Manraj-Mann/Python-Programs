# loops - iterate over 

i = 0
while ( i != 10):
    print(i)
    i += 2

guess = ""
org = "Word"
points = 10

while (guess != org and points > 0 and points >= len(guess) ):

    points -= len(guess)
    guess = input("Enter the guess : ")

if ( points > 0 and  points >= len(guess)):
    print("You won , points : " + str(points))
else : 
    print("You Lost")


# for loops 

from numpy import arange


for i in "Code Forge":
    print(i)

for i in range(10 , 20):
    print(i)

# not work
for i in range (100 , -100):
    print(i)

for i in range(1 , -11 , -1):
    print(i)

array = [1,2,2,4]
for index in range(len(array)):
    print(array[index])