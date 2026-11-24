#find duplicate data in list
a = [10,20,20,30,20,40,40,40]
print(a)
b=[]
for x in a:
    if x not in b:
        b.append(x)
print("Unique Data:",b)