for i in range(1,4):
    for j in range(1,4):
        if(i==j and i+j==4):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()

# for i in range(1,4):
#     for j in range(1,4):
#         if(i==j and (i!=1 and j!=1) and (i!=3 and j!=3)):
#             print("$",end=" ")
#         else:
#             print("*",end=" ")
#     print()