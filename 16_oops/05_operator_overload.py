class point:
    def __init__(self , x, y):
        self.x = x
        self.y = y  

    def sum(self, p):
        return point((self.x + p.x), (self.y + p.y))


    def print_point(self):

        print (f"x is {self.x} and y is {self.y}")
        # print("f x is {self.x} and y is {self.y}")


    def __add__(self, p ):
       return point((self.x + p.x), (self.y + p.y))
    

p1 = point(3, 2)
p2 = point(6, 3)

p = p1.sum(p2)
# print(p.print_point())
p = p1 + p2 # we overeloaded the + operator by writting __add__ function means that ### + ko hun direct nhi likh skte jaise a + b pr agr mai use kru command  def __add__ to mai aisa  skta hu
p.print_point()    




# some other operator like  def __add__ are-----
#__sub__     =      (-)   subtract
#__mul__     =      ( *)  multiply
#__truediv__ =       (/)   slash
#__eq__      =       (==)
#__ne__      =       (!=)