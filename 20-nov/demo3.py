# prog. for IndexError Exception
try:
    a=[1,2,3,4,5]
    print(a[6])
except IndexError:
    print("List index is not defined.")
