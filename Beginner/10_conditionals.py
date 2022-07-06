from doctest import REPORT_UDIFF


hungry = True


# simple if else 

if(hungry):

    print("I woke up")

else : 
    
    print("I am sleeping")

hungry = False

if(hungry):

    print("I woke up")

else : 
    
    print("I am sleeping")

# if else ladder


hungry = True
food = False

if ( hungry and food):
    print("Eat food")

elif (hungry and (not food)) : 
    print("go to market")

else : 

    print("Doomed")


# maxnums example 

def max_nums(num1  , num2 , num3):

    if(num1 >= num2 and num1 >= num3):   
        return num1
    elif (num2 >= num1 and num2 >= num3):
        return num2
    else:
        return num3
    
print(max_nums(2 , 5 , 2))


# user input manipulation

n1 = float(input("Enter num 1 : "))
n2 = float(input("Enter num 2 : "))
op = input("Enter operator : ")

if(op == "+"):
    print(n1+n2)
elif ( op == "-"):
    print(n1-n2)
elif ( op == "*"):
    print(n1*n2)
elif ( op == "/"):
    print(n1/n2)
else: print("failure")