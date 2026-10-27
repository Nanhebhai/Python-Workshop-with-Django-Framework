n="10"
x=int(n)
print(type(x))

n="10aaaa"     #String to int incompatible
x=int(n)      #valueError
print(type(x))