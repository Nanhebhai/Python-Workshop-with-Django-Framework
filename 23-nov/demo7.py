#Object Oriented programming in Python
# Class

class product:
    def setdata(self):
        self.code=101
        self.name="printer"
        self.qty=5
        self.price=20000
    def display(sel):
        print("code=",sel.code)
        print("name=",sel.name)
        print("qty=",sel.qty)
        sel.totalprice=sel.qty*sel.price
        print("Totalprice=",sel.totalprice)
    # def display(self):
    #     print("code=",self.code)
    #     print("name=",self.name)
    #     print("qty=",self.qty)
    #     self.totalprice=self.qty*self.price
    #     print("Totalprice=",self.totalprice)

obj=product()
obj.setdata()
obj.display()
