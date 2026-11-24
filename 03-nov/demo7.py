#list with membership operator
a = [3,23,56,7,8,9]
s=int(input("Enter Data to be Search:"))
res= s in a
if(res):
    print("Data Found")
else:
    print("Not Found") 