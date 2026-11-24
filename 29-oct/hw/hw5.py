 #prog. for 1/1!+1/2!+.........+1/n!
n = int(input("Enter any number"))
s =0 
a =1
f =1
while(a<=n):
    f=f*a
    print("fact=",f)
    div = 1/a
    print("div=",div)
    s=s+div
    print("sum=",s)
    a+=1

print("Total sum is",s)
