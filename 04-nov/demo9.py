# s="python is a programming language."
# search=input("Enter search string.")
# x=s.find(search)
# if(x==0):
#     print("String found")
# else:
#     print("String not found")

#string with membership operator
s="python is a programming language."
search=input("Enter search string.")
res=search in s
print(res)
if(res):
    print("String found")
else:
    print("not found")