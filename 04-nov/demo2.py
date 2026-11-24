#Lower case to Upper case
s="abc"
for x in s:
    print(chr(ord(s[0]-32)))#chr for ASCII to character 

#upper case to lower case
s="ABC"
for x in s:
    print(chr(ord(x)+32))