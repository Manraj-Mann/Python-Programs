class student:

    def __init__(self , name , major , gpa , is_failed) :
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_failed = is_failed
    
    def printdata(self):
        print("Name : " + self.name)
        print("Major : " + self.major)
        print("Gpa : " + str(self.gpa))
        print("Is_failed : " + str( self.is_failed))

class specialstudent( student):
    
    def honors(self):
        print("Honours")

stud = student("Gurjot" , "CSE" , 8.5 , False)

print(stud)
print(stud.name)
stud.printdata()

spstud = specialstudent("Gurjot" , "CSE" , 8.5 , False)

spstud.honors()