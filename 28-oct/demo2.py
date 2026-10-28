# per = int(input("enter percentage"))
# yr = int(input("enter passing year"))
# res = (per>=75  and yr==2024)

# print(res)

per = int(input("enter percentage"))
yr = int(input("enter passing year"))
# res = not(per>=75  and yr==2024)
res = (per>=75  or yr==2024)
# res = not(per>=75  and yr==2024)

print(res)