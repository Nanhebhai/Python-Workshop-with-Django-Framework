#Function with passing argument

class product:
    def setdata(self,a,b,c,d):
        self.code=a
        self.name=b
        self.qty=c
        self.price=d
   
    def display(self):
        print("code=",self.code)
        print("name=",self.name)
        print("qty=",self.qty)
        self.totalprice=self.qty*self.price
        print("Totalprice=",self.totalprice)

obj1=product()
obj1.setdata(101,"printer",2,20000)
obj1.display()
obj2=product()
obj2.setdata(102,"pen drive",3,200)
obj2.display()
