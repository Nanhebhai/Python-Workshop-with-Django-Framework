#2.hierarchical Inheritance
# one base class multiple derived classes
class area:
    def seta(self):
        self.a=3.5
        return(self.a)
    def setb(self):
        self.b=4.5
        return(self.b)
class circle(area):
    def display(self):
        self.r=area.seta(self)
        self.x=3.14*self.r*self.r
        print("Area of circle:",self.x)

class rectangle(area):
    def demo(self):
        self.l=area.seta(self)
        self.b=area.setb(self)
        print("Area of Rectangle:",self.l*self.b)
    
obj1=circle()
obj1.display()

obj1=rectangle()
obj1.demo()