
# general catch - catch all exceptions

# try: 
#     number = int(input("Number is : "))
#     print(number)
# except:
#     print("Invalid")

from decimal import DivisionByZero


try: 

    number = int(input("Number is : "))
    print(number)
except DivisionByZero:
    print("Divide by zero")
except ValueError:
    print("Invalid")
