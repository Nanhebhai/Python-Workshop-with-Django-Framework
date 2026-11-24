try:
    a=(10,20,30)
    # a.append(40)
except:
    print("Tuple is immutable")
else:
    b=list(a)
    b.append(40)
    a=tuple(a)
    print(a)
finally:
    print("program Ends here.")