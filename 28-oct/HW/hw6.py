#write a program to find middle among three number.
a = int(input("Enter 1st NUmber:"))
b = int(input("Enter 2nd Number:"))
c = int(input("Enter 3rd Number:"))

if((a>b and a<c)or(a<b and a>c)):
    print("a is th middle number")
if((b>a and b<c)or(b<a and b>c)):
    print("b is the middle number")
if((c>a and c<b)or(c<a and c>b)):
    print("c is the middle number")