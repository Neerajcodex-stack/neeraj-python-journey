def sum(a,b):
    print("hey i am summing")
    c = a + b
    global z         #please modify global z   use to modify global keyword z
    z = 0           # this will refer to global z and not create a local variable
    return c


z = 3 
print(sum(3 , 12))
print(z)




# interview question 
# can you modify a global variable inside a function??????
### yes ! but we have to use global.........chatgpt.com should check it....





