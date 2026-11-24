#check string is palindrome or not
s = input("Enter any string:")
res=""
for x in s:
    res=x+res
print("res",res)
if(res==s):
    print("Palindrome String.")
else:
    print("not palindrome.")