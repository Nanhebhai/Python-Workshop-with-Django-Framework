#Types of Inheritance
#1.Single Inheritance 
# one base class one derive class

class area:
    def seta(self):
        self.a=3.5
        return(self.a)
class circle(area):
    def display(self):
        self.r=area.seta(self)
        self.x=3.14*self.r*self.r
        print("Area of circle:",self.x)
    
obj1=circle()
obj1.display()

