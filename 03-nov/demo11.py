#Unpacking in Tuple
name=("ram","naman","kanak","raman","ragu")
print(name)
# (x,y,*z)=name
# (*x,y,z)=name
(x,*y,z)=name
print(x)
print(y)
print(z)