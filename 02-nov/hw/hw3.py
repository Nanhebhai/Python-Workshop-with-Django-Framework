#find duplicate element in list.
a =[]
n = int(input("Enter limit of the list:"))
for i in range(0,n):
    value=int(input("Enter list element:"))
    a.append(value)

duplicates=[]
print(a)
for i in a:
    if a.count(i)>1 and i not in duplicates:
        duplicates.append(i)

print("Duplicates Elements:",duplicates)