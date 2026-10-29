yr = int(input("Enter year:"))

if(yr%400==0 or yr%4==0):
    print("Year is leap year.")
elif(yr%100 == 0):
    print("year is not a leap year.")
else:
    print("Year is not a leap year.")