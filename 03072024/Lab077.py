#Polymorphism
#method override
class shape:
    def area(self):
        print("This is area")

class rectangle():
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width

class circle():
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
cir=circle(2)
print(cir.area())
rec=rectangle(2,3)
print(rec.area())


