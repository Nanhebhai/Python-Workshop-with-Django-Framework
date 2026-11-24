# #Strip function
# s="   test    "
# print(len(s))
# print(len(s.strip()))

# #replace Function
# s="python is a programming language.python is a smart language."
# print(s)
# x= s.replace("python","java")
# print(x)

# s="python is a programming language.python is a smart language."
# print(s)
# x= s.replace("python","java",1)
# print(x)

# #Split Function
# s="2026-11-04"
# print(s)
# a=s.split("-")
# print(type(a))
# print(a)
# s1=a[2]+"/"+a[1]+"/"+a[0]
# print(s1)
# print(type(s1))

# #using split function
# s="logo.jpg" #sunset.jpg
# print(s)
# a=s.split(".")
# print(a)
# s1="sunset."+a[1]
# print(s1)

# #Using replace function
# s="logo.jpg" #sunset.jpg
# print(s)
# a=s.replace("logo","sunset")
# print(a)

#prog. for count number of word
s=input("Enter any String:")
print(s)
word=s.split(" ")
print(word)
# print(len(word))
count=0
charcount=0
for x in word:
    count+=1
    charcount+=len(x)
print("count is",count)
print(charcount)
