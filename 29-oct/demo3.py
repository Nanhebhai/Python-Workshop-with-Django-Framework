#prog. for arithmatic operations

print("Press 1 for sum")
print("Press 2 for sub")
print("Press 3 for multi")
print("Press 4 for div")

ch = int(input("Enter your choice:"))
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
if(ch==1):
    c = a+b
    print("sum=",c)
elif(ch==2):
    c = a-b
    print("sub=",c)
elif(ch==3):
    c = a*b
    print("multi=",c)
elif(ch==4):
    c = a/b
    print("div=",c)
else:
    print("Invalid choice.")