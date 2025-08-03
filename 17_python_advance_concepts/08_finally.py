a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
 
 
try: 
     c = a/b
     print(c)

except Exception as e:
     print(e) 


# this is always executed no matter if try compltly executes or not hamesa rhega chae error aaye ya na aaye ye rhega "this is always executed"
finally:
     print("this is always executed")      
     