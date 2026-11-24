#Bubble Sorting
a=[5,4,3,2,1]
print("Before sorting")
print(a)

for i in range(0,len(a)):
    for j in range(0,len(a)-1-i):
        if(a[j]>a[j+1]):
            t=a[j]
            a[j]=a[j+1]
            a[j+1]=t
print("After Sorting.")
print(a)