class employee : 

    company = "asus"  #class attribute 

    def __init__(self, salary, name,bond, company):
        self.salary = salary
        self.name = name
        self.bond = bond
        self.company = company
    def get_salary(self): 
        return self.salary 

    def get_info(self):
        print(f"the name of the employee is {self.name}.salary is {self.salary}. the bond is for {self.bond}years")    

e1 = employee(34000,"john doe",4,"tesla")
print(e1.company) #will always print a instance attribute whenever  present 
print(employee.company) # this can print class attribute 

#OBJECT INTROSEPTION

print(dir(e1))      #all the attributes can find by it

