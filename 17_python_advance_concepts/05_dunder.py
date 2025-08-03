
    # DUNDER METHOD (DUNDER )=== DOUBLE UNDERSCORE(__)

class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"
    

    def __repr__(self):
        return f"name : {self.name} \n salary: {self.salary}"
    
    def __len__(self):         # magic method use to know the total digit or number in word
        return len(self.name)






e = Employee("Neeraj", 456736)
print(len(e)) 
print(e.name , e.salary)      
print(str(e))
print(repr(e))        