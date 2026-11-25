# Function Overriding
class base:
    def display(self):
        print("base class called")
class derived:
    def display(self):
        base.display(self)#function within function call
        print("derived class called")
obj=derived()
obj.display()


# class base:
#     def display(self):
#         print("base class called")
# class derived:
#     def display(self):
#         print("derived class called")
# obj=base()
# obj.display()


# class base:
#     def display(self):
#         print("base class called")
# class derived:
#     def display(self):
#         print("derived class called")
# obj=derived()
# obj.display()