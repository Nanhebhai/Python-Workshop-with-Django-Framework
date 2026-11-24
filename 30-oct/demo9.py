#nested for in loop 

# for i in range(1,3):
#     for i in range(1,3):
#         print("*",end=" ")
#     print()

# for i in range(1,3):
#     for j in range(1,3):
#         print(j,end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(6,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the limit: "))
# for i in range(n,0,-1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n = int(input("Enter the limit: "))
# a=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(a,end=" ")
#         a+=1
#     print()

n = int(input("Enter limit: "))
for i in range(1,n+1):
    for k in range(n,i,-1):
        print(end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    
# n = int(input("Enter limit: "))
# for i in range(1,n+1):
#     for k in range(n,i,-1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# n = int(input("Enter limit: "))
# for i in range(1,n+1):
#     for k in range(n,i,-1):
#         print(end=" ")
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()