# Create a String
s="123abc"
print(type(s))
print(s)

#for in loop
for x in s:
    print(x)

#For in loop with range function
for i in range(0,len(s)):
    print("index-",i,"data-",s[i])