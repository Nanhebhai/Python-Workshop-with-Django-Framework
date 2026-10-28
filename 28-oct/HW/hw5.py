# Write a program to reverse three digit integer number.
a = int(input("Enter any three digit number:"))

b = a%10
a = a//10
c = b*100

b = a%10
a = a//10
c =( b*10 )+ c

b = a%10
a = a//10
c = b + c

print("Reverse number is ",c)