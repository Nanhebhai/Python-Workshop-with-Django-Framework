#Find sum and product of list element
a =[]
n = int(input("Enter limit of the list:"))
for i in range(0,n):
    value=int(input("Enter list element:"))
    a.append(value)
print(a)

sum=0
for i in range(0,n):
    sum+=a[i]
print("Sum is",sum)