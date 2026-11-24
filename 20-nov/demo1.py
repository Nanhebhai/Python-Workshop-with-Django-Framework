#prg. for Exception handling
try:
    n=5
    res=n/2
    print(res)
except ZeroDivisionError:
    print("Number must be greater than zero.")
print("test program")

# try:
#     n=5
#     res=n/0
#     print(res)
# except ZeroDivisionError:
#     print("Number must be greater than zero.")
# print("test program")