# Decorator is a function that take a function, it creates a new function inside its body (wrapper). then it returns that new function 



def decorator(func):
    def wrapper():
        print("I am about to execute a function....")
        func()
        print("i have executed this function...")
    return wrapper    





def say_hello():
    print("hello!")

f = decorator(say_hello)
f()  