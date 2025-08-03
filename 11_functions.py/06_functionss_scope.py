def sum(a , b):
    # a and b are local variables
    c = a + b
    z = 1     #it creates a local variable called z which is destroyed after this function returns
    return c



def greet():
     z = 32 #local variable
     print("hello")


z = 8 #z is a global variable
print(sum(4 , 6))
print(z)