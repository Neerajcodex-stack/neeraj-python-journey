class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    #instance method (default)
    def print_info(self):
        info = f"the name is {self.name} and the salary is {self.salary}"    
        print(info)
   
    #### static method (code run without using self command)
    @staticmethod
    def sum(a, b):
        return a + b
    

    ### class methods
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company



e1 = Employee("jack", 3455)
e2 = Employee("jill", 3456)        
# print(Employee.company)
# print(Employee.name)

# e1.print_info()
# e2.print_info()
# print(e2.sum(5, 26))


# e1.print_company()       #  making this commamad can be  use to check whether change or not 
print(Employee.company)
e1.change_company("Acer")
# e1.print_company()
print(Employee.company) 


                 

