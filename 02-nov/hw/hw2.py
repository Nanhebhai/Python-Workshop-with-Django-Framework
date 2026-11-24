#Find 1st and 2nd max in list
a =[]
n = int(input("Enter limit of the list:"))
for i in range(0,n):
    value=int(input("Enter list element:"))
    a.append(value)

print(a)
b=a[0]
for i in a:
    if(b>i):
        pass
    else:
        b=i

print(b," is the largest in list.")
a.remove(b)
print(a)

b=a[0]
for i in a:
    if(b>i):
        pass
    else:
        b=i
print(b," is the second largest in list.")