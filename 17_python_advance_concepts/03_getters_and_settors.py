class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
    def first_name(self):
        l = self.name.split(" ")
        return l[0]
    def set_first_name(self, first):
        l = self.name.split(" ")
        new_name = f"{first} {l[1]}"
        self.name = new_name    

# e = Employee("jack doe", 34000)
# print(e.first_name())
# e.set_first_name("john")                #@decode it
# print(e.name)                      # we are changeing the name withiout changing surname #@correct it chat gpt

e = Employee("jack doe", 34000)
print(e.first_name())                   #@decode it
e.first_name = "john"            # again apni form mai le aaye isse code krke
print(e.name)                     


