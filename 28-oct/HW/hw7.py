#write a program to calculate profit and loss with cost price and selling price.
cp = int(input("Enter cost price of the product:"))
sp = int(input("Enter selling price of the product:"))

if(sp>cp):
    profit = sp-cp
    print("Total profit is",profit)
if(sp<cp):
    loss = cp-sp
    print("Total loss is",loss)