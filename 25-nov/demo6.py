#constructor overriding
class base:
    def __init__(self):
        print("base class called")
class derived:
    def __init__(self):
        super().__init__()#base class constructor
        print("derived class called")
obj=derived()
