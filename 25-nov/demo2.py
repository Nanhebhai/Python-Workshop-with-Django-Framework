#operator Overloading
from multipledispatch import dispatch

@dispatch(int)
def add(x):
    print(x+x)

@dispatch(int,float)
def add(x,y):
    print(y+x)

@dispatch(float,int,float)
def add(x,y,z):
    print(x+y+z)

add(10)
add(10,20)
add(10,20,30)