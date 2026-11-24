#Linear/Sequential search
a=[2,12,8,9,10,5]
print(a)
s=int(input("Enter data to be search:"))
found=0
for i in range(0,len(a)):
    if(a[i]==s):
        found=1
        break
if(found==1):
    print("Element Found at ",(i+1),"Position.")
else:
    print("Element not found.")
