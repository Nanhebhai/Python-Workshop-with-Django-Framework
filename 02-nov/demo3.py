#List
a = [10,20,30,40,50]

print(type(a))
print(a)

#number function
print("Max:",max(a))
print("Min:",min(a))
print("Sum:",sum(a))
print("Length:",len(a))

a.append(0)
print(a)

a.append(60)
print(a)

a.pop()
print(a)

a.pop(5)
print(a)

a.pop(9)