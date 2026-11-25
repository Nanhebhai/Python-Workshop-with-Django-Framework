#Abstract class
from abc import ABC,abstractmethod

class base(ABC):#Abstract class
    @abstractmethod
    def display(self):
        pass
class derived(base):
    def display(self):
        print("display called in derived")

obj=derived()
obj.display()