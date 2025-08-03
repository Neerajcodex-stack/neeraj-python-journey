class employee : 
    def __init__(self, salary, name,bond):
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self): 
        return self.salary 

    def get_info(self):
        print(f"the name of the employee is {self.name}.salary is {self.salary}. the bond is for {self.bond}years")    

e1 = employee(34000,"john doe",4)
print(e1.get_salary())
e1.get_info()



class student :
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def show_info(self):
     print(f"Name: {self.name}, Age:{self.age}")

#object
s1 = student("Neeraj", 22)
s1.show_info()    
   





   
