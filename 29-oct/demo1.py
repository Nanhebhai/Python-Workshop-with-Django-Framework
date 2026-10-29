#maximum out of 3 number
a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))
c = int(input("Enter 3rd number"))

if(a>b & a>c):
    print("a is greater thsn b and c")
elif(b>c):
    print("b is greater than c and a")
else:
    print("c is greater than a and b")