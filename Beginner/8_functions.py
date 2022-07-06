# def = keyword for functions 

# syntax: def function_name( parameters ) :  

def say_hi( v):

    print("hi "+v , end="\n") # intendation is imp 

def say_hi_TO( v , TO):

    print("hi "+v + " FROM " + TO, end="\n") # intendation is imp 



say_hi("Manraj") # call to function 


# flow of funtions - line by line 

print("top")
say_hi("User ")
print("Bottom")

say_hi_TO('Mike' , 'Steve')