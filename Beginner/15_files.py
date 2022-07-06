# open("filename" , "mode")

emp_file = open("employee.txt" , "r")

#general methods 

print(emp_file.readable())
print(emp_file.mode)

# reading file 

print(emp_file.read())
emp_file.close()

# readline 

emp_file = open("employee.txt" , "r")
print(emp_file.readline())

# create list of all lines

print(emp_file.readlines())
emp_file.close()


 # writing in file 

emp_file = open("employee.txt" , "a")

print(emp_file.mode)

print(emp_file.writable())

emp_file.write("\nI wrote it ")

emp_file.close()