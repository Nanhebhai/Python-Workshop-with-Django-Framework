a=[10,20,30]
b=[11,12,13,10]
print(a)
print(b)
c=a.copy()
print(c)

c.append(40)
print(a)
print(c)

#Delete reference
del b
print(b)