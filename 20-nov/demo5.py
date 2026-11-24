try:
    n=5
    m=int(input("enter any number."))
    res=n/m
    print(res)
except ZeroDivisionError:
    print("Number must be greater than zero.")
else:
    print("result=",res)
finally:
    print("Program end here.")
print("test program")