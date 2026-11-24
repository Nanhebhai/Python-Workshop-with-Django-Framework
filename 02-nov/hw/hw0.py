#write a program to find diff-diff area using menu driven program.
while True:
    print("press 0 for exit-")
    print("press 1 for finding area of circle-")
    print("press 2 for finding rectangle of circle-")
    print("press 3 for finding triangle of circle-")
    ch = int(input("Enter your choice:"))
    if(ch==0):
        print("thank you")
        break
    elif(ch==1):
        value=float(input("Enter Radius of circle:"))
        result=3.14*value*value
        print("Radius of circle is",result)
    elif(ch==2):
            value1=float(input("Enter base of triangle:"))
            value2=float(input("Enter height of the triangle:"))
            result=1/2*value1*value2
            print("Area of triangle is ",result)
    elif(ch==3):
            value1=float(input("Enter length of rectangle:"))
            value2=float(input("Enter breadth of the rectangle:"))
            result=value1*value2
            print("Area of rectangle is ",result)
    else:
            print("Invalid choice")