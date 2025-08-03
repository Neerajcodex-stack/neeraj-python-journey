# '''a = int(input("Enter a number between 1 and 10:"))



# match(a) :
#     case 1:
#         print("you won a charger")

#     case 3:
#         print("you won iphone")    

#     case 4:
#         print("you won a $3")

#     case _:                                       #for default score we have to use _:
#         print("Better luck next time")       '''     











# day = int(input("Enter a number from 1 to 7:"))

# match(day):
    
#     case 1 :
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3 :
#         print("Wednesday")
#     case 4:
#         print("thurasday")
#     case 5:
#         print("friday")
#     case 6:
#         print("saturaday")
    
#     case _:
#         print("invalid")
#  '''                                                        	1.	🔢 Number Sign Checker
# User se ek number le aur batao:
# 	•	Positive hai
# 	•	Negative hai
# 	•	Zero hai'''




'''number = int(input("enter a number :"))
         

if(number<0):
    print("negative number")
elif(number>0):
    print("positive number")
else:
    print("its mean value 0")     ''' 




'''number = int(input("enter a number"))

if(number %2 == 0):
    print("even number")

else:
    print("odd") '''






'''k password input lo
	•	Rules:
	•	Agar length < 6 → “Weak Password”
	•	Agar length 6–10 and only alphabets → “Moderate Password”
	•	Agar length > 10 and has special chars → “Strong Password” '''


'''password = (input("give a password input:"))
         if len(password)<6:   
      print("weak password")
elif password.isalpha():
      print("moderate password")
elif password.isalnum():
      print("strong password")        
else:
      print("passowor word unclear")    '''   





lottery = (input("enter a random word:"))

match lottery :
    case ("guess"):
        print("hurray you won a phone")

    case ("matter"):
        print("you won a cooker")  

    case ("overpowered"):
        print("you won a box")  

    case _:
        print("better luck next time")      


