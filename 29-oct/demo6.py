#check the number is armstrong or not
n = int(input("Enter any number:"))
temp = n
res = 0
while(n!=0):
    a = n%10
    res = (a**3)+res
    n = n//10

if(temp == res):
    print("Number is armstrong.")
else:
    print("number is not armstrong.")