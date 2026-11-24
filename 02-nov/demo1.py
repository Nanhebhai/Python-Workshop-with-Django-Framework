 # prg. for unit conversion
while True:
    print("Press 0 for exit")
    print("press 1 for km to meter")
    print("press 2 for meter to km")
    print("press 3 for faherenheit to celcius")
    print("press 4 for celcius to faherenheit")
    print("press 5 for kilogram to gram")
    print("press 6 for gram to kilogram")
    ch=int(input("Enter your choice:"))
    if ch==0:
        print("Thank you")
        break
    value = float(input("Enter the value:"))
    
    if(ch==1):
        result=value*1000
        print("result=",result,"meter")
    elif(ch==2):
        result=value/1000
        print("result=",result,"kilometer")
    elif(ch==3):
        result=(value*9/5)+32
        print("result=",result,"celcius")
    elif(ch==4):
        result=(value-32)*5/9
        print("result=",result,"faherenheit")
    elif(ch==5):
        result=value*1000
        print("result=",result,"gram")
    elif(ch==6):
        result=value/1000
        print("result=",result,"kilogram")
    else:
        print("Invalid choice.")