n = int(input("Enter limit: "))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n,0,-1):
    for k in range(i,n+1):
        print(end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print()