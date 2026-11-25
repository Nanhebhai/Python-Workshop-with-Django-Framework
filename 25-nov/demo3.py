#operator Overloading
class number:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):#__add__() is predefined function
        x=self.x+other.x
        y=self.y+other.y
        return(x,y)

obj1=number(10,20)
obj2=number(30,40)
obj3=obj1+obj2   #calling __add__()
print(obj1+obj2)