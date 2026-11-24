#Parameterized constructor
# Destructor in python
class product:
    def __init__(self,a,b):#Parameterized constructor
        self.qty=a
        self.price=b
        print("Total=",(self.qty*self.price))

    def __del__(self):
        print("objeect Destroyed")

obj1=product(3,500)
obj2=product(5,300)
obj3=product(6,400)
