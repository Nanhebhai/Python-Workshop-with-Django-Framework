#prog. for print division on the basis of percentage
per = float(input("Enter your percentage"))

if(per>=60):
    print("1st division")
elif(per>=45 and per<60):
    print("2nd division")
elif(per>=33 and per<45):
    print("3rd division")
else:
    print("fail")