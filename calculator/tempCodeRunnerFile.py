
try:
    a = int(input("Enter a  first number: 😌  "))

    b = int(input("enter a second number: ☺️  "))
    print("what kind of operation do you want to perform. \npress + for addition 🔴 \npress - for substraction 🟢\npress / for division 🟡 \npress * for multipication ⚫")
    o = input("Enter Operation: ☺️ ")
    match o:
     case "+":
          print(f"the result is: {a + b} ✅ ")

     case "-":
          print(f"the result is: {a - b} ✅ ")
     case "/":
          print(f"the result is: {a / b} ✅")
     case "*":
          print(f"the result is: {a * b} ✅")    
     case _:
          print(f" there was an error ")
except Exception as e:
  print("Enter a valid value of a and b ❌  ")  
