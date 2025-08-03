class animal:
    location = "india"
    def __init__(self, name ):
        self.name = name 
    def speak(self):
        print("speaking now......")

class dog(animal):
    def speak (self):
        super().speak()   #we are using the speak function of the  parent class 
        print("woof!")



d = dog("scissor")
d.speak()
print(d.location)