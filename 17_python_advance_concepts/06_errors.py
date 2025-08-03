
#  by these we can solve the differnt types of errors in our python in this lec we know abhout the exception handling in python here we know if i enetr a number like 1 2 4 34 anything it cause sum of this butttt what happen if i put a alphabet like a b c instead of digit then the program will crashed in this lec we are talking about the these type of errrors and resolve it 






         
# while True:    

#     try:          
#          a = int(input("Enter a number 1: "))
#          b = int (input("enter a number 2:"))


#          print(f"the division is {a / b}")


#     except ValueError:
#          print("hey dont do this ")


#     except ZeroDivisionError:

#          print("please dont divide by 0")    


#     except Exception as e:
#          print("unknown error occured!", e)



# ERROR RAiSE KRNE KA COMMAND HAI JISSE MAI KISI KO BHI ROK SKTA HU APNE CODE MAI CHEDAKHANI KRNE SE LIKE IN GOOGLE CONSOLE I CANT ABLE TO ADD ANY CODE SAME HERE 


a = int(input("Enter a number 1: "))
b = int (input("enter a number 2:"))


print(f"the division is {a / b}")


if b == 0:        # LETS TAKING COMMAND AS 0 IT WAS ANYTHING WE WANT TO AVOID 
    raise ValueError("please dont divide by 0")

print(f"the division is {a / b}")
   







