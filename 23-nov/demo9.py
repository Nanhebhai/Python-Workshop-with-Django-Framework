#Constructor is special member function in python.
# it define by magic method __init__()

class product:
    def __init__(self):#default constructor
        self.qty=5
        self.price=1000
        print("Total=",(self.qty*self.price))

obj=product()
