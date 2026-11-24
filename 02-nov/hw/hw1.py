#Find Even/Odd in list
a =[]
n = int(input("Enter limit of the list:"))
for i in range(0,n):
    value=int(input("Enter list element:"))
    a.append(value)

print(a)
for i in a:
    if(i%2==0):
        print(i,"is an even number.")
    else:
        print(i,"is an odd number.")
