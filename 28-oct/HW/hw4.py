#Write a program to find maximum among 3 numbers using multiple if .

a = int(input("Enter 1st NUmber:"))
b = int(input("Enter 2nd Number:"))
c = int(input("Enter 3rd Number:"))

if(a>b and a>c):
    print("a is greater than b and c")
if(b>c and b>a):
    print("b is greater than a and c")
if(c>a and c>b):
    print("c is greater than a and c")