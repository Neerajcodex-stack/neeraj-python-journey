# class: class is a blueprint or a template. eg. form for an exam that contains name, age , electives, fathers name etc

# object: object is a specific instance created from the template (class). eg. from which contains the data for john doe



class employee : 
    company  = "HP"


    def get_salary(self):  #self is important here because self is the refrance the object of the class which being created..
        print(self)
        return 34000
    
e1 = employee() #an object of class employee is created here
print(e1.get_salary())    # employee e's get salary method is called

e2 = employee()
print(e2.get_salary())
print(e2.company)